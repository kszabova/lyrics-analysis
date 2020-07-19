import lyrics_analysis

def tag_rhymes(lyrics, tag):
    """
    Wraps rhyming words of lyrics inside given HTML tag.
    :param lyrics: Lyrics where lines are separated by newlines
    :param tag: Tag that rhyming words should be wrapped in.
        Without brackets, i.e. 'strong' instead of '<strong>'.
    :return: Lyrics separated by newlines with appropriately
        tagged words
    """

    split_lines = lyrics.splitlines()
    _, rhyming_lines = lyrics_analysis.evaluation.rhymes(split_lines, return_rhymes=True)

    lines = []
    for i, line in enumerate(split_lines):
        if i in rhyming_lines and line.split():
            words = line.split()
            words[-1] = "<" + tag + ">" + words[-1] + "</" + tag + ">"
            lines.append(" ".join(words))
        else:
            lines.append(line)

    return "\n".join(lines)


