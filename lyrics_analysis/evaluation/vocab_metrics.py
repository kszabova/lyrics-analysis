def count_unique_words(lyrics):
    """
    Counts unique words in lyrics.
    :param lyrics: List of strings representing song text
    :return: Number of unique words
    """
    words = ' '.join(lyrics).split()
    word_set = set(words)
    return len(word_set)


