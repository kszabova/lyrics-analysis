class Song:
    """
    Object containing the data about a single song.
    """

    def __init__(self,
                 lyrics,
                 genre,
                 artist,
                 title):
        self._lyrics = lyrics
        self._genre = genre
        self._artist = artist
        self._title = title

    @property
    def lyrics(self):
        return self._lyrics

    @property
    def genre(self):
        return self._genre

    @property
    def artist(self):
        return self._artist

    @property
    def title(self):
        return self._title


def get_song_from_dictionary(dict):
    """
    Creates a Song object given a dictionary.
    It is assumed that the dictionary contains
    keys "lyrics", "genre" and "artist".
    :param dict: Dictionary containing data about a song
    :return: Song object
    """

    return Song(
        dict["lyrics"],
        dict["genre"],
        dict["artist"]
    )
