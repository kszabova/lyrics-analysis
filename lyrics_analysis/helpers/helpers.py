import itertools
import ijson
import gensim
import nltk

import lyrics_analysis

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


def _get_mean_set_score(set, metric):
    """
    Calculates the mean score of all songs in set using the specified metric.
    :param set: Generator that yields Song objects
    :param metric: Metric used for calculating the score
    :return: Mean score of all songs
    """

    scores = []
    for song in set():
        scores.append(metric(song.lyrics))

    return sum(scores) / len(scores)


def _get_generator_from_file(file):
    """
    Takes a JSON file and creates a generator that
    yields all songs form it as Song objects.
    :param file: Source file with songs
    :return: Generator yielding Song objects
    """
    def generator():
        with open(file) as f:
            songs = ijson.items(f, 'item')
            for song in songs:
                yield lyrics_analysis.Song(
                    song["lyrics"], song["genre"], song["artist"], song["title"]
                )

    return generator


def _get_tfidf_dict(file):
    """
    Parses a corpus a creates a dictionary containing
    words appearing in the text.
    :param file: Text corpus in JSON format containing
        all fields necessary to create a Song object
    :return: gensim.corpora.Dictionary object
    """

    lyrics_generator = _get_generator_from_file(file)
    dictionary = gensim.corpora.Dictionary(
        " ".join(song.lyrics).lower().split() for song in lyrics_generator()
    )

    # remove stop words and words that only occur once
    stoplist = nltk.corpus.stopwords.words('english')
    stop_ids = [
        dictionary.token2id[stopword]
        for stopword in stoplist
        if stopword in dictionary.token2id
    ]
    punct_list = ". , ' \" & - _ ! ? = / ; :".split()
    punct_ids = [
        dictionary.token2id[punct]
        for punct in punct_list
        if punct in dictionary.token2id
    ]
    once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.items() if docfreq == 1]
    dictionary.filter_tokens(stop_ids + once_ids + punct_ids)
    dictionary.compactify()

    return dictionary
