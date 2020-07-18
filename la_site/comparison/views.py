import random
import gensim

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from .models import Artist, Song, Score
from .forms import SongForm
from .artists import Artists

import lyrics_analysis

def evaluate_lyrics(request, score_id):
    score = get_object_or_404(Score, pk=score_id)

    scores = []
    for artist in Artists.ARTISTS:
        artist_songs = Score.objects.filter(song__artist=artist[0])
        scores.append(random.choice(artist_songs) if artist_songs else None)

    artists = []
    for i, artist in enumerate(Artists.ARTISTS):
        artists.append((artist[0], artist[1], scores[i]))

    return render(
        request,
        'comparison/evaluate_lyrics.html',
        {
            'score': score,
            'artists': artists
        }
    )

# load models necessary for score evaluation
dict = gensim.corpora.Dictionary.load("./comparison/static/models/tfidf.dict")
model = gensim.models.TfidfModel.load("./comparison/static/models/tfidf.model")
def get_lyrics(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            artist_name = form.cleaned_data['artist']
            title = form.cleaned_data['title']
            genre = form.cleaned_data['genre']
            lyrics = form.cleaned_data['lyrics']

            # calculate scores
            lyrics_lines = lyrics.splitlines()
            rhyme_score = lyrics_analysis.evaluation.rhymes(lyrics_lines)
            tfidf_score = lyrics_analysis.evaluation.tf_idf(lyrics_lines, dict, model)

            artist = Artist.objects.filter(name=artist_name).first()
            if not artist:
                artist = Artist.create(artist_name)
                artist.save()

            song = Song.create(artist, title, genre, lyrics)
            song.save()

            score = Score.create(song, rhyme_score, tfidf_score)
            score.save()

            artist.rhyme_score_avg = (F('number_of_songs') * F('rhyme_score_avg') + rhyme_score) / (F('number_of_songs') + 1)
            artist.tfidf_score_avg = (F('number_of_songs') * F('tfidf_score_avg') + tfidf_score) / (F('number_of_songs') + 1)
            artist.number_of_songs = F('number_of_songs') + 1
            artist.save()

            return HttpResponseRedirect(reverse('comparison:evaluate_lyrics', args=(score.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    return render(request, 'comparison/submit_lyrics.html', {'form': form})
