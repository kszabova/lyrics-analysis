def count_unique_words(lyrics):
    """
    Counts unique words in lyrics.
    :param lyrics: List of strings representing song text
    :return: Number of unique words
    """
    words = ' '.join(lyrics).split()
    word_set = set(words)
    return len(word_set)


def tf_idf(lyrics, dictionary, tfidf):
    """
    :returns the average tf_idf score for the words in the song lyrics.
    :param lyrics: List of rows of song lyrics
    :param dictionary: gensim.Dictionary object from the desired corpus
    :param tfidf: gensim.Tfidf object from the desired corpus
    :return:
    """
    lyrics = " ".join(lyrics).lower().split()
    tfidf_score =tfidf[dictionary.doc2bow(lyrics)]
    return sum(map(lambda score: score[1], tfidf_score)) / len(tfidf_score) if len(tfidf_score) else 0

