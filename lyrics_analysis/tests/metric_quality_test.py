from lyrics_analysis import helpers

def calculate_metric_quality(metric, eval_sets):
    """
    Calculates how well the metric ranks evaluation sets
    compared to the expected ranking.
    :param metric: The metric to be evaluated
    :param eval_sets: List of lists of evaluation set generators.
        Every inner list is considered to have equal score.
        Lists are ordered from lowest score.
    :return: Number between 0 and 1 representing how
        well the metric ranked the evaluation sets.
    """

    # validate arguments
    if len(eval_sets) <= 1:
        raise ValueError("There must be at least two sets to compare.")

    # save the relation
    # creates a dictionary indexed by (score_class, set_index)
    # where the value is a list of all (score_class, set_index) sets
    # that should have a higher score than the key
    higher_scores = {}
    for score_class in range(len(eval_sets)):
        for set_index in range(len(eval_sets[score_class])):
            higher_scores[(score_class, set_index)] = [
                (x, y)
                for x in range(score_class)
                for y in range(len(eval_sets[x]))
            ]

    # calculate the score for each set
    scores = []
    for equal_score_sets in eval_sets:
        current_scores = []
        for set in equal_score_sets:
            current_scores.append(helpers._get_mean_set_score(set, metric))
        scores.append(current_scores)

    # compare the calculated scores to expected scores
    correct_relations = []
    for key, value in higher_scores.items():
        for expected_relation in value:
            if scores[key[0]][key[1]] > scores[expected_relation[0]][expected_relation[1]]:
                correct_relations.append(1)
            else:
                correct_relations.append(0)

    return sum(correct_relations)/len(correct_relations)

