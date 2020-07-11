from django import forms

class SongForm(forms.Form):
    artist = forms.CharField(label='artist', max_length=200)
    title = forms.CharField(label='title', max_length=200)
    genre = forms.ChoiceField(label='genre', choices=[
        ('RAP', 'rap'),
        ('POP', 'pop'),
        ('RCK', 'rock'),
        ('RNB', 'r-b'),
        ('CTR', 'country')
    ])
    lyrics = forms.CharField(label='lyrics', widget=forms.Textarea)
