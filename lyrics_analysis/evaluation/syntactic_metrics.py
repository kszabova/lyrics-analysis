import nltk
from lyrics_analysis.helpers import helpers


def proportion_content_words(lyrics):
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


def content_words_line_end(lyrics):
    """
    Calculates the proportion of lines that end
    with a content word.
    :param lyrics: List of strings representing song text
    :return: Proportion of lines ending with a content word
    """
    content_tags = ['CD', 'FW', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS',
                     'RB', 'RBR', 'RBS', 'VB', 'VBG', 'VBN', 'VBP', 'VBZ']
    last_words = helpers._get_last_words(lyrics)
    tagged = nltk.pos_tag(last_words)
    print(tagged)
    content_words= list(filter(lambda tag: tag[1] in content_tags, tagged))
    return len(content_words) / len(last_words)
