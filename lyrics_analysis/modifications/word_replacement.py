import random


def replace_last_words_on_line(lyrics, words, probability=0.1):
    """
    For each line, replaces the last word with one of words
    with given probability.
    :param lyrics: List of strings
    :param words: A single word or a list of words
        that will be used to replace original words
    :param probability: Probability that a word will be replaced
    :return: Modified lyrics
    """

    # if words param is a single word, make it into an array
    if type(words) == str:
        words = [words]

    new_lyrics = []
    for line in lyrics:
        rand = random.random()
        if rand <= probability and len(line) > 0:
            word_to_replace = random.choice(words)
            split_line = line.split()[:-1]           # discard the last word
            split_line.append(word_to_replace)      # add the new word
            new_lyrics.append(' '.join(split_line)) # add the new line to list
        else:
            new_lyrics.append(line)

    return new_lyrics
