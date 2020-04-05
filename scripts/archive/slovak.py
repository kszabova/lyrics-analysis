import ijson
import json
import pycld2 as cld2

def remove_bad_chars(s):
    chars_to_replace = [chr(c) for c in range(ord('\x70'), ord('\x9f') + 1)]
    for char in chars_to_replace:
        s = s.replace(char, '')
    return s

with open("../data/song_lyrics_music_only.json") as songs:

    with open("../data/slovak_lyrics", 'w') as out_file:

        objects = ijson.items(songs, "item")
        for object in objects:

            try:
                _, _, details = cld2.detect(''.join(object["lyrics"]))
                lang_detected = details[0][0]
                if lang_detected == "SLOVAK":
                    out_file.write(json.dumps(object))
            except Exception as e:
                try:
                    s = remove_bad_chars(''.join(object["lyrics"]))
                    is_reliable, text_bytes_found, details = cld2.detect(s)
                    lang_detected = details[0][0]
                    if lang_detected == "SLOVAK":
                        out_file.write(json.dumps(object))
                except Exception as e:
                    print(e)