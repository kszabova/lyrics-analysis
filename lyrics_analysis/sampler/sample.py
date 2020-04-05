import ijson
import json
import random


def sample(n, source, dest, total_n=None, shuffle=False):
    """
    Takes n random objects from the source file and stores it in dest.

    The source file is expected to be an array of JSON objects with
    a 'lyrics' field that contains an array of strings.

    The result will be stored as a list of lists of strings.

    :param n: How many examples to take
    :param source: Path to source file
    :param dest: Path to destination file (will be overwritten)
    :param total_n: Total number of examples in the source file; if specified, objects
        will be taken from the entire file
    :param shuffle: Whether or not rows are to be shuffled
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
    examples = []
    while counter < n:
        try:
            with open(source) as src:
                objects = ijson.items(src, "item")
                for object in objects:
                    rand = random.random()
                    if rand <= rate:
                        try:
                            lyrics = object["lyrics"]
                            if shuffle:
                                random.shuffle(lyrics)
                            examples.append(lyrics)
                            counter += 1
                            if counter == n:
                                break  # stop generating new examples
                        except KeyError:
                            raise RuntimeError("File does not have correct format")
                    else:
                        pass

        except Exception as e:
            raise e

    # write the examples into the output file
    try:
        with open(dest, 'w') as dst:
            dst.write(json.dumps(examples))
    except Exception as e:
        raise e

