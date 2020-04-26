def _get_last_words(lines):
    """
    Helper method that takes a list of strings and
    returns a list of last words in each strings.
    If string does not contain any word, it is skipped.
    :param lines: List of strings representing lines
    :return: List of last words in each line
    """
    return [words[-1] for words in [line.split() for line in lines] if len(words) > 0]


def _get_last_n_phonemes(words, n, arpabet):
    """
    For each word in words retrieves the last n phonemes.
    :param words: List of words
    :param n: How many phonemes from the end of the
        word should be returned
    :param arpabet: Dictionary with word pronunciations
    :return: List of tuples containing the last n phonemes
        for each word
    """

    return words.map(lambda word: arpabet.get(word, [])[-n:])
