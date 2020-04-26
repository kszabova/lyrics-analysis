import nltk
from lyrics_analysis import helpers

ARPABET = nltk.corpus.cmudict.dict()

def rhymes(lyrics, rhyme_level=2, arpabet=ARPABET):
    """
    Calculates the proportion of lines that rhyme with
    the previous line.
    :param lyrics: List of strings representing song lyrics
    :param rhyme_level: How many phonemes at the end of lines
        should be equal to be considered a rhyme
    :return: Proportion of rhyming lines
    """

    last_words = [word.lower() for word in helpers._get_last_words(lyrics)]
    if len(last_words) <= 1:
        return 0                # check if we have at least 2 lines to parse

    rhyme_count = 0
    # get pronunciation; default is no syllables if cmudict doesn't recognize the word
    prev_word = arpabet.get(last_words[0], [])
    for word in last_words[1:]:
        cur_word = arpabet.get(word, [])
        # count pronunciations that match in the last rhyme_level phonemes
        matches = [pron_prev[-rhyme_level:] == pron_cur[-rhyme_level:]
                   for pron_prev in prev_word for pron_cur in cur_word]
        # increase rhyme counter if there was at least one match
        rhyme_count += 1 if any(matches) else 0
        # change previous word
        prev_word = cur_word
    return rhyme_count / len(last_words)
