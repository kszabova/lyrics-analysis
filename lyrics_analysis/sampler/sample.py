import ijson
import json
import random


def sample_n_songs_from_generator(n, src_generator, total_n=None, filter=(lambda _: True)):
    """
    Selects n random examples from src_stream.
    The result will be returned as a generator.

    :param n: How many examples to take
    :param src_generator: Function that creates a generator with source data
    :param total_n: Total number of examples in the source file; if specified,
        objects will be taken from the entire file
    :param filter: Function returning a bool that determines
        if the example should be considered for selection
    :returns: Generator yielding n random examples
    """

    # check if arguments are valid
    if n <= 0:
        raise ValueError("Parameter n must be at least 1.")
    if type(n) != int:
        raise TypeError("Parameter n must be an integer.")
    if total_n:
        if type(total_n) != int:
            raise TypeError("Parameter total_n must be an integer.")
        if total_n <= 0:
            raise ValueError("Parameter total_n must be at least 1.")

    # probability at which an example will be selected
    rate = 0.1
    if total_n:
        rate = n / total_n

    counter = 0
    # the inner loop iterates over source data until it has enough
    # examples or until it reaches the end;
    # the outer loop ensures that it will iterate over all the
    # data enough times
    while counter < n:
        try:
            gen = src_generator()
            for song in gen:
                rand = random.random()
                if rand <= rate and filter(song):
                    try:
                        yield song
                        counter += 1
                        if counter == n:
                            break  # stop generating new examples
                    except KeyError:
                        raise RuntimeError("File does not have correct format")
                else:
                    pass

        except Exception as e:
            raise e

