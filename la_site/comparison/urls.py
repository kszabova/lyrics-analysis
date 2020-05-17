from django.urls import path
from . import views

app_name = 'comparison'
urlpatterns = [
    path('', views.get_lyrics, name='get_lyrics'),
    path('<int:score_id>/evaluate/', views.evaluate_lyrics, name='evaluate_lyrics'),
]
