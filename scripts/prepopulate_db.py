#
# ADDING INITIAL DATA TO DATABASE
#
# Clear the existing database
# Navigate to the folder lyrics-analysis/la_site and run the command `python manage.py dbshell`.
# Type the following to clear the database and reset id counter:
#    remove from comparison_score;
#    remove from comparison_song;
#    remove from sqlite_sequence where name = 'comparison_score';
#    remove from sqlite_sequence where name = 'comparison_song';
#
# Adding new data
# Run the command `python manage.py shell`.
# In the shell, type the following to populate the database.
#
# import ijson
#
# from models import Song, Score
# import lyrics_analysis
#
# def retrieve_songs(file):
#     with open(file) as f:
#         songs = ijson.items(f, 'item')
#         for song in songs:
#             yield (
#                 song["lyrics"], song["genre"], song["artist"], song["title"]
#             )
#
# FILE = '../data/cleaned/eval_set_100_lyrics.json'
# for lyrics, genre, artist, title in retrieve_songs(FILE):
#     lyrics = '\n'.join(lyrics)
#     song = Song.create(artist, title, genre, lyrics)
#     song.save()
#     score = Score.create(song)
#     score.save()
#