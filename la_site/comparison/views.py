from django.shortcuts import render, get_object_or_404

from .models import Score

def evaluation(request, score_id):
    score = get_object_or_404(Score, pk=score_id)
    return render(request, 'comparison/evaluate_lyrics.html', {'score': score})
