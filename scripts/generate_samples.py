import lyrics_analysis.sampler
import ijson
import json
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--sizes', default="100,1000,10000", help="Sizes of randomly generated samples")
args = parser.parse_args()

# returns a generator that yields items
# from source file
def create_generator_from_file(path):

    def src_generator():
        with open(path) as file:
            for item in ijson.items(file, "item"):
                yield item

    return src_generator


sizes = [int(size) for size in args.sizes.split(',')]
data_dir = "../data/cleaned/"
file_prefix = "eval_set_"

# create sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics.json"
    examples = list(lyrics_analysis.sample_n_songs_from_generator(size, create_generator_from_file(source)))
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating lyrics sets.")

# create shuffled sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics_shuffled.json"
    examples = list(lyrics_analysis.sampler.sample_n_songs_from_generator(size, create_generator_from_file(source)))
    for example in examples:
        random.shuffle(example["lyrics"])
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating shuffled lyrics sets.")

# create sets of random texts
for size in sizes:
    source = data_dir + "song_lyrics_non_music.json"
    dest = data_dir + file_prefix + str(size) + "_random.json"
    examples = list(lyrics_analysis.sample_n_songs_from_generator(size, create_generator_from_file(source)))
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating random text sets.")

