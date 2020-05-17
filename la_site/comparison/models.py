from django.db import models


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


class Score(models.Model):

    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    rhyme_score = models.FloatField(default=0)

    def __str__(self):
        return str(self.song)
