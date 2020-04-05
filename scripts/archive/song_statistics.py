import ijson
import json
import pprint

class Statistics():

    def __init__(self, filename):
        self._data = {}
        self._filename = filename

    def parse(self):
        """
        Parses file self._filename and calculates statistics.
        """

        # if data has already been parsed, do nothing
        if self._data:
            return

        stats = {
            "genres": {},
            "artists": {},
            "global_stats": {
                "songs": 0,
                "lines": 0,
                "words": 0
            }
        }
        try:
            with open(self._filename) as file:
                objects = ijson.items(file, "item")

                # compute metrics
                for object in objects:

                    lines = len(object["lyrics"])
                    words = sum([len(line.split()) for line in object["lyrics"]])

                    genre = object["genre"]
                    stats["genres"][genre] = stats["genres"].get(genre, {"artists": {}})
                    genre_obj = stats["genres"][genre]
                    genre_obj["songs"] = genre_obj.get("songs", 0) + 1
                    genre_obj["lines"] = genre_obj.get("lines", 0) + lines
                    genre_obj["words"] = genre_obj.get("words", 0) + words
                    genre_obj["is_music"] = genre_obj.get("is_music", 0)
                    if object["is_music"] != "false":
                        genre_obj["is_music"] += 1

                    artist = object["artist"]
                    stats["artists"][artist] = stats["artists"].get(artist, 0) + 1
                    stats["genres"][genre]["artists"][artist] = stats["genres"][genre]["artists"].get(artist, 0) + 1

                    # update global stats
                    stats["global_stats"]["songs"] += 1
                    stats["global_stats"]["lines"] += lines
                    stats["global_stats"]["words"] += words

                # calculate averages for each genre
                for genre, genre_stats in stats["genres"].items():
                    genre_stats["avg_line_length"] = genre_stats["words"] / genre_stats["lines"]
                    genre_stats["avg_lines"] = genre_stats["lines"] / genre_stats["songs"]
                    genre_stats["avg_words"] = genre_stats["words"] / genre_stats["songs"]

                # calculate global averages
                stats["global_stats"]["avg_line_length"] = stats["global_stats"]["words"] / stats["global_stats"]["lines"]
                stats["global_stats"]["avg_lines"] = stats["global_stats"]["lines"] / stats["global_stats"]["songs"]
                stats["global_stats"]["avg_words"] = stats["global_stats"]["words"] / stats["global_stats"]["songs"]

                self._data = stats

        except IOError as e:
            print("Exception occurred: ", e)

    def show(self, include_stats=False, include_artists=False, global_only=False):
        """
        Summarizes genre-specific lyrics statistics.

        :keyword include_stats: if True, includes metrics
            such as average word count for each genre
        :keyword include_artists: if True, lists artists
            and their song count for each genre
        :keyword global_only: if True, skips genre-specific
            statistics and only returns global ones

        :returns: python dictionary with specified data
        """

        return self._data

stats = Statistics("../data/song_lyrics_no_duplicates.json")
stats.parse()
with open("../data/clean_stats.json", 'w') as out_file:
    pprint.pprint(stats.show(), out_file)


