def _get_last_words(lines):
    """
    Helper method that takes a list of strings and
    returns a list of last words in each strings.
    If string does not contain any word, it is skipped.
    :param lines: List of strings representing lines
    :return: List of last words in each line
    """
    return [words[-1] for words in [line.split() for line in lines] if len(words) > 0]
