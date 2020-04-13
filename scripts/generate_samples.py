from lyrics_analysis import sampler
import ijson
import json
import random

# returns a generator that yields items
# from source file
def create_generator_from_file(path):

    def src_generator():
        with open(path) as file:
            for item in ijson.items(file, "item"):
                yield item

    return src_generator


sizes = [100, 1000, 10000]
data_dir = "../data/cleaned/"
file_prefix = "eval_set_"

# create sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics.json"
    examples = []
    for example in sampler.sample_n_songs_from_generator(size, create_generator_from_file(source)):
        examples.append(example)
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating lyrics sets.")

# create shuffled sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics_shuffled.json"
    examples = []
    for example in sampler.sample_n_songs_from_generator(size, create_generator_from_file(source)):
        examples.append(example)
    random.shuffle(examples)
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating shuffled lyrics sets.")

# create sets of random texts
for size in sizes:
    source = data_dir + "song_lyrics_non_music.json"
    dest = data_dir + file_prefix + str(size) + "_random.json"
    examples = []
    for example in sampler.sample_n_songs_from_generator(size, create_generator_from_file(source)):
        examples.append(example)
    with open(dest, 'w') as out_file:
        json.dump(examples, out_file)
print("Finished creating random text sets.")

