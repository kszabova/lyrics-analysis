import itertools
import nltk

def count_unique_words(lyrics):
    """
    Counts unique words in lyrics.
    :param lyrics: List of strings representing song text
    :return: Number of unique words
    """
    words = ' '.join(lyrics).split()
    word_set = set(words)
    return len(word_set)


def proportion_parts_of_speech(lyrics):
    """
    Calculates the proportion of nouns, adjectives,
    verbs and adverbs.
    :param lyrics: List of strings representing song text
    :return: Proportion of content words
    """
    content_tags = ['CD', 'FW', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS',
                     'RB', 'RBR', 'RBS', 'VB', 'VBG', 'VBN', 'VBP', 'VBZ']
    text = ' '.join(lyrics)
    tokens = nltk.tokenize.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    content_words = list(filter(lambda tag: tag[1] in content_tags, tagged))
    return len(content_words) / len(tagged)

