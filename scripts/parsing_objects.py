import ijson
import pprint

with open("../data/song_lyrics10.json") as file:
    objects = ijson.items(file, "item")

    pprint.pprint(next(objects))

