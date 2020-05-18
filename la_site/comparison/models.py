from django.db import models

# TODO: How to import the module properly?
MODULE_PATH = "C:/Users/kristina/Documents/School/Rocnikac/lyrics-analysis/lyrics_analysis/__init__.py"
MODULE_NAME = "lyrics_analysis"
import importlib
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
lyrics_analysis = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = lyrics_analysis
spec.loader.exec_module(lyrics_analysis)

class Song(models.Model):

    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=3, choices=[
        ('RAP', 'rap'),
        ('POP', 'pop'),
        ('RCK', 'rock'),
        ('RNB', 'r-b'),
        ('CTR', 'country')
    ])
    lyrics = models.TextField()

    def __str__(self):
        return str(self.artist) + ": " + str(self.title)

    @classmethod
    def create(cls, artist, title, genre, lyrics):
        song = cls(artist=artist, title=title, genre=genre, lyrics=lyrics)
        return song


class Score(models.Model):

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rhyme_score = models.FloatField(default=0)

    def __str__(self):
        return str(self.song)

    @classmethod
    def create(cls, song):
        lyrics = song.lyrics.splitlines()
        rhyme_score = lyrics_analysis.evaluation.rhymes(lyrics)

        score = cls(song=song, rhyme_score=rhyme_score)
        return score
