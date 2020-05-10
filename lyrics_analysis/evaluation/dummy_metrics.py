import random

def eval_random(lyrics):
    """
    Generates a random score between 0 and 1.
    :param lyrics: Lyrics to evaluate
    :return: Score
    """
    return random.random()

def eval_line_length(lyrics):
    """
    Generates score representing the average number
    of words per line.
    :param lyrics: Lyrics to be evaluated
    :return: Score
    """
    words = sum((len(line.split()) for line in lyrics))
    lines = len(lyrics)
    return words / lines