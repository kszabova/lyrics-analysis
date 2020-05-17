import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Score
from .forms import SongForm

def evaluate_lyrics(request, score_id):
    score = get_object_or_404(Score, pk=score_id)

    # find a song with a better score
    better_scores = Score.objects.filter(rhyme_score__gte=score.rhyme_score)
    better_score = random.choice(better_scores)

    # find a song with a worse score
    worse_scores = Score.objects.filter(rhyme_score__lte=score.rhyme_score)
    worse_score = random.choice(worse_scores)

    return render(
        request,
        'comparison/evaluate_lyrics.html',
        {
            'score': score,
            'better': better_score,
            'worse': worse_score
        }
    )

def get_lyrics(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.save()
            score = Score.create(song)
            score.save()

            return HttpResponseRedirect(reverse('comparison:evaluate_lyrics', args=(score.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    return render(request, 'comparison/submit_lyrics.html', {'form': form})
