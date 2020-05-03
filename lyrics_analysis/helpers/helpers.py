import itertools

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
    :return: List of lists of tuples containing the last n phonemes
        for each word for each possible pronunciation
    """

    phonemes = []
    for word in words:
        phonemes.append(
            list(map(lambda pron: tuple(pron[-n:]), arpabet.get(word, [])))
        )
    return phonemes


INTERCHANGEABLE_PHONEMES = {
    'AA': ['AA', 'AE', 'AH'],
    'AE': ['AE', 'AA', 'AH'],
    'AH': ['AH', 'AA', 'AE'],
    'B': ['B', 'P'],
    'P': ['B', 'P'],
    'CH': ['CH', 'JH'],
    'JH': ['CH', 'JH'],
    'D': ['D', 'T', 'DH'],
    'DH': ['D', 'DH'],
    'T': ['D', 'T', 'TH'],
    'TH': ['T', 'TH'],
    'F': ['F', 'V'],
    'V': ['F', 'V'],
    'G': ['G', 'K'],
    'K': ['G', 'K'],
    'SH': ['SH', 'ZH'],
    'ZH': ['SH', 'ZH'],
    'M': ['M', 'N'],
    'N': ['M', 'N'],
    'R': ['R', 'L'],
    'L': ['R', 'L'],
    'S': ['S', 'Z'],
    'Z': ['S', 'Z']
}

def _get_alternative_pronunciations(pronunciation):
    """
    Creates a list of pronunciations with all possible interchangeable
    combinations of phonemes.
    :param pronunciation: Tuple of phonemes
    :return: List of tuples containing interchangeable pronunciations
    """
    alternative_phonemes = [
        INTERCHANGEABLE_PHONEMES.get(phoneme, [phoneme]) for phoneme in pronunciation
    ]
    return list(itertools.product(*alternative_phonemes))
