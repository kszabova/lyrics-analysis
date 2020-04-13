import json
import lyrics_analysis.evaluation

def evaluate_set(set, metric):
    """
    Computes average score of a set.
    :param set: Path to file with data
    :param metric: Which metric to use
    :return: Average of scores
    """
    try:
        with open(set) as src:
            texts = json.load(src)
    except Exception as e:
        raise e
        exit()

    scores = [metric(text["lyrics"]) for text in texts]
    return sum(scores) / len(scores)

if __name__ == "__main__":
    random = lyrics_analysis.evaluation.eval_random
    line_length = lyrics_analysis.evaluation.eval_line_length
    print("Random evaluation:")
    print("Songs:\t\t", evaluate_set("../data/cleaned/eval_set_100_lyrics.json", random))
    print("Shuffled songs:\t", evaluate_set("../data/cleaned/eval_set_100_lyrics_shuffled.json", random))
    print("Random texts:\t", evaluate_set("../data/cleaned/eval_set_100_random.json", random))
    print()
    print("Line length evaluation:")
    print("Songs:\t\t", evaluate_set("../data/cleaned/eval_set_100_lyrics.json", line_length))
    print("Shuffled songs:\t", evaluate_set("../data/cleaned/eval_set_100_lyrics_shuffled.json", line_length))
    print("Random texts:\t", evaluate_set("../data/cleaned/eval_set_100_random.json", line_length))
