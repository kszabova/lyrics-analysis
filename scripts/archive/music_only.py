import ijson
import json

with open("../data/song_lyrics_music_only.json") as file:
    objects = ijson.items(file, "item")

    with open("../data/song_lyrics_music_only.json", 'a') as out_file:
        out_file.write("[\n")
        for object in objects:
            if object["is_music"] == "true":
                out_file.write(json.dumps(object))
                out_file.write(",\n")
        out_file.write("]")