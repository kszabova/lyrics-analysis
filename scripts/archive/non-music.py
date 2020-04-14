import ijson
import json

with open("../../data/cleaned/song_lyrics_clean.json") as file:
    objects = ijson.items(file, "item")

    with open("../../data/cleaned/song_lyrics_non_music.json", 'w') as out_file:
        out_file.write("[\n")
        for object in objects:
            if object["is_music"] == "false":
                out_file.write(json.dumps(object))
                out_file.write(",\n")
        out_file.write("]")