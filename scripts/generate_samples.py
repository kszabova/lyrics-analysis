from lyrics_analysis import sampler

sizes = [100, 1000, 10000]
data_dir = "../data/cleaned/"
file_prefix = "eval_set_"

# create sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics.json"
    sampler.sample(size, source, dest)
print("Finished creating lyrics sets.")

# create shuffled sets of lyrics
for size in sizes:
    source = data_dir + "song_lyrics_english_only.json"
    dest = data_dir + file_prefix + str(size) + "_lyrics_shuffled.json"
    sampler.sample(size, source, dest, shuffle=True)
print("Finished creating shuffled lyrics sets.")

# create sets of random texts
for size in sizes:
    source = data_dir + "song_lyrics_non_music.json"
    dest = data_dir + file_prefix + str(size) + "_random.json"
    sampler.sample(size, source, dest)
print("Finished creating random text sets.")

