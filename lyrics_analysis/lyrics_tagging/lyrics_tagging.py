import lyrics_analysis

def tag_rhymes(lyrics, cls):
    """
    Wraps rhyming words of lyrics inside a class tag.
    :param lyrics: Lyrics where lines are separated by newlines
    :param cls: Class name that rhyming words should be wrapped in.
    :return: Lyrics separated by newlines with appropriately
        tagged words
    """

    split_lines = lyrics.splitlines()
    _, rhyming_lines = lyrics_analysis.evaluation.rhymes(split_lines, return_rhymes=True)

    lines = []
    for i, line in enumerate(split_lines):
        if i in rhyming_lines and line.split():
            words = line.split()
            words[-1] = '<div class="' + cls + '">' + words[-1] + '</div>'
            lines.append(" ".join(words))
        else:
            lines.append(line)

    return "\n".join(lines)


