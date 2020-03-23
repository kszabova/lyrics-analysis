import pycld2 as cld2
import ijson

def detect_language(lyrics_list):
    lyrics = ''.join(lyrics_list)
    return cld2.detect(lyrics)

with open("../data/song_lyrics10.json") as file:
    objects = ijson.items(file, "item")

    for object in objects:
        is_reliable, text_bytes_found, details = detect_language(object["lyrics"])
        if details[0][0] == "ENGLISH":
            print(details)
