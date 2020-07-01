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


def remove_last_word_on_line(lyrics, probability=0.1):
    """
    Removes the last word on line with the given probability.
    :param lyrics: List of strings
    :param probability: Probability that the last word will be removed
    :return: Modified lyrics
    """

    new_lyrics = []
    for line in lyrics:
        rand = random.random()
        if rand <= probability and len(line) > 0:
            # split the line into words, remove the last one and join them with spaces
            new_line = ' '.join(line.split()[:-1])
            new_lyrics.append(new_line)
        else:
            new_lyrics.append(line)

    return new_lyrics


def remove_words_on_line(lyrics, probability=0.1):
    """
    Removes each word in the lyrics with the given probability.
    :param lyrics: List of strings
    :param probability: Probability of a word being removed
    :return: Modified lyrics
    """

    new_lyrics = []
    for line in lyrics:
        modified_line = [word for word in line.split() if random.random() > probability]
        new_lyrics.append(" ".join(modified_line))
    return new_lyrics
