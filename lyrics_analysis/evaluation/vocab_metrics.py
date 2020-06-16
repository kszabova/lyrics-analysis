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

    :param lyrics:
    :param dictionary:
    :param tfidf:
    :return:
    """
    lyrics = " ".join(lyrics).lower().split()
    tfidf_score =tfidf[dictionary.doc2bow(lyrics)]
    return sum(map(lambda score: score[1], tfidf_score)) / len(tfidf_score)

