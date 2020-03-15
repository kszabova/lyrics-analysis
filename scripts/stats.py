import ijson
import pprint

with open("song_lyrics10.json") as file:
    objects = ijson.items(file, "item")

    pprint.pprint(next(objects))

