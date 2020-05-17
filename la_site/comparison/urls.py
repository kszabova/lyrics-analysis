from django.urls import path
from . import views

app_name = 'comparison'
urlpatterns = [
    path('', views.get_lyrics, name='get_lyrics')
]
