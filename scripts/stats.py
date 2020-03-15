import ijson
import json
from pprint import pprint

def calc_average_line_length(words, lines):
    return words / lines

def calc_average_song_lines(lines, songs):
    return lines / songs

def calc_average_song_words(words, songs):
    return words / songs

# these are the statistics we want to get
stats = {
    "genres": {},
    "artists": {},
    "global_stats": {
        "songs": 0,
        "lines": 0,
        "words": 0
    }
}

with open("../data/song_lyrics.json") as file:
    objects = ijson.items(file, "item")

    for object in objects:

        lines = len(object["lyrics"])
        words = sum([len(line.split()) for line in object["lyrics"]])

        genre_stats = object["genre"]
        stats["genres"][genre_stats] = stats["genres"].get(genre_stats, {})
        genre_obj = stats["genres"][genre_stats]
        genre_obj["songs"] = genre_obj.get("songs", 0) + 1
        genre_obj["lines"] = genre_obj.get("lines", 0) + lines
        genre_obj["words"] = genre_obj.get("words", 0) + words

        artist = object["artist"]
        stats["artists"][artist] = stats["artists"].get(artist, 0) + 1

        # update global stats
        stats["global_stats"]["songs"] += 1
        stats["global_stats"]["lines"] += lines
        stats["global_stats"]["words"] += words

# calculate averages for each genre
for genre, genre_stats in stats["genres"].items():
    genre_stats["avg_line_length"] = calc_average_line_length(genre_stats["words"], genre_stats["lines"])
    genre_stats["avg_lines"] = calc_average_song_lines(genre_stats["lines"], genre_stats["songs"])
    genre_stats["avg_words"] = calc_average_song_words(genre_stats["words"], genre_stats["songs"])

# calculate global averages
stats["global_stats"]["avg_line_length"] = calc_average_line_length(stats["global_stats"]["words"], stats["global_stats"]["lines"])
stats["global_stats"]["avg_lines"] = calc_average_song_lines(stats["global_stats"]["lines"], stats["global_stats"]["songs"])
stats["global_stats"]["avg_words"] = calc_average_song_words(stats["global_stats"]["words"], stats["global_stats"]["songs"])

with open("stats.txt", 'w') as file:
    json.dump(stats, file, indent=4)
