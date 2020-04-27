import nltk
from lyrics_analysis import helpers

ARPABET = nltk.corpus.cmudict.dict()

def rhymes(lyrics, rhyme_level=2, max_distance=2, arpabet=ARPABET):
    """
    Calculates the proportion of lines that rhyme with
    another line at a distance of at most max_distance
    :param lyrics: List of strings representing song lyrics
    :param rhyme_level: How many phonemes at the end of lines
        should be equal to be considered a rhyme
    :param max_distance: Lines at what distance are still
        considered a rhyme
    :param arpabet: Dictionary with word pronunciations
    :return: Proportion of rhyming lines
    """

    last_words = [word.lower() for word in helpers._get_last_words(lyrics)]
    last_phonemes = helpers._get_last_n_phonemes(last_words, rhyme_level, arpabet)

    # store all rhyming lines in a dictionary
    rhyming_lines = {}
    for i, prons in enumerate(last_phonemes):
        for pron in prons:
            rhyming_lines[pron] = rhyming_lines.get(pron, [])
            rhyming_lines[pron].append(i)

    # add a point for each line that rhymes with a line at at most max_distance
    rhyme_count = 0
    for i, prons in enumerate(last_phonemes):
        considered_lines = [i - d for d in range(1, max_distance + 1)] + \
                           [i + d for d in range(1, max_distance + 1)]
        for pron in prons:
            if set(rhyming_lines[pron]).intersection(set(considered_lines)):
                rhyme_count += 1
                break

    # calculate the proportion of rhyming lines
    return rhyme_count / len(last_words)
