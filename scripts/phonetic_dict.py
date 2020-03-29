import nltk
import ijson

arpabet = nltk.corpus.cmudict.dict()
with open("../data/song_lyrics10.json") as file:
    objects = ijson.items(file, "item")

    for object in objects:
        lyrics = object["lyrics"]
        phonetic = [
            [arpabet[word.lower()][0] for word in line.split()] for line in lyrics
        ]
        print(phonetic)

