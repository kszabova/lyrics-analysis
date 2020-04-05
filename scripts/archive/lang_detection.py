import pycld2 as cld2
import ijson
import json

# removes all characters in the specified range;
# the range was determined empirically
def remove_bad_chars(s):
    chars_to_replace = [chr(c) for c in range(ord('\x70'), ord('\x9f') + 1)]
    for char in chars_to_replace:
        s = s.replace(char, '')
    return s


with open("../data/song_lyrics_music_only.json") as file:
    objects = ijson.items(file, "item")

    with open("../data/song_lyrics_english_only.json", 'w') as out_file:
        wrong_encoding = 0
        out_file.write("[\n")

        languages = {}
        english_lyrics = 0

        for object in objects:

            try:
                is_reliable, text_bytes_found, details = cld2.detect(''.join(object["lyrics"]))
                lang_detected = details[0][0]
                languages[lang_detected] = languages.get(lang_detected, 0) + 1
                if lang_detected == "ENGLISH":
                    english_lyrics += 1
                    out_file.write(json.dumps(object))
                    out_file.write(",\n")
            except Exception as e:
                try:
                    s = remove_bad_chars(''.join(object["lyrics"]))
                    is_reliable, text_bytes_found, details = cld2.detect(s)
                    lang_detected = details[0][0]
                    languages[lang_detected] = languages.get(lang_detected, 0) + 1
                    if lang_detected == "ENGLISH":
                        english_lyrics += 1
                        out_file.write(json.dumps(object))
                        out_file.write(',\n')
                except Exception as e:
                    print(e)
        out_file.write("]")

    # write language counts
    with open("../data/languages.json", 'w') as lang_file:
        json.dump(languages, lang_file)

    print(english_lyrics)
