import argparse

from lyrics_analysis import helpers

parser = argparse.ArgumentParser()
parser.add_argument('--source', default=r'../data/cleaned/song_lyrics_english_only.json', type=str)
parser.add_argument('--modelfile', default=r'../models/tfidf.model', type=str)
parser.add_argument('--dictfile', default=r'../models/tfidf.dict', type=str)
args = parser.parse_args()

dict, model = helpers._get_tfidf_dict(args.source)
dict.save(args.dictfile)
model.save(args.modelfile)
