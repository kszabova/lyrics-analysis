import pycld2 as cld2
import ijson
import json

with open("../data/song_lyrics_music_only.json") as file:
    objects = ijson.items(file, "item")

    with open("../data/song_lyrics_english_only.json", 'a') as out_file:
        out_file.write("[\n")
        for object in objects:
            is_reliable, text_bytes_found, details = cld2.detect(
                "".join(object["lyrics"])
            )
            if details[0][0] == "ENGLISH":
                out_file.write(json.dumps(object))
                out_file.write(",\n")
        out_file.write("]")
