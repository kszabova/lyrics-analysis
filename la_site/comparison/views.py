from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Score
from .forms import SongForm

def evaluation(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    return render(request, 'comparison/evaluate_lyrics.html', {'score': score})

def get_lyrics(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/evaluate/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SongForm()

    return render(request, 'comparison/submit_lyrics.html', {'form': form})
