class Song:
    """
    Object containing the data about a single song.
    """

    def __init__(self,
                 lyrics,
                 genre,
                 author):
        self._lyrics = lyrics
        self._genre = genre
        self._author = author

    @property
    def lyrics(self):
        return self._lyrics

    @property
    def genre(self):
        return self._genre

    @property
    def author(self):
        return self._author
