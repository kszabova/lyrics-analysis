#
# Generate evaluation sets with modified lyrics.
# The songs will be randomly selected from the whole dataset.
# Their lyrics can be modified with an arbitrary function.
#

import json
import ijson
import functools

from lyrics_analysis import modifications
from lyrics_analysis import sampler

# returns a generator that yields items
# from source file
def create_generator_from_file(path):

    def src_generator():
        with open(path) as file:
            for item in ijson.items(file, "item"):
                yield item

    return src_generator

sizes = [100, 1000, 10000]
funcs = [
    modifications.remove_last_word_on_line,
    functools.partial(modifications.replace_last_words_on_line, words=["porcupine", "armadillo", "anteater"])
]
func_names = ["_removed_words", "_replaced_words"]

path = "../data/cleaned/"
prefix = "eval_set_"

for size in sizes:
    for func, func_name in zip(funcs, func_names):
        source = path + "song_lyrics_english_only.json"
        dest = path + prefix + str(size) + func_name + ".json"
        examples = []
        for example in sampler.sample_n_songs_from_generator(size, create_generator_from_file(source)):
            example["lyrics"] = func(example["lyrics"])
            examples.append(example)
        with open(dest, 'w') as out_file:
            json.dump(examples, out_file)
        print("Finished generating samples for function " + func_name + " for size " + str(size))
