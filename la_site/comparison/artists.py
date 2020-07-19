from .models import Artist

class Artists:
    artist_names = [
        "Z-Mane",
        "Zola Jesus",
        "Awa",
        "Zip K.",
        "Boston"
    ]
    artist_genres = [
        "pop",
        "rock",
        "r-n-b",
        "rap",
        "country"
    ]
    artist_objects = [Artist.objects.get(name=name) for name in artist_names]

    ARTISTS = list(zip(artist_objects, artist_genres))
    ARTISTS = sorted(ARTISTS, key=lambda o: (o[0].tfidf_score_avg + o[0].rhyme_score_avg)/2, reverse=True)

    @classmethod
    def add_artist(cls, score):
        extended_artists = []
        avg = (score.tfidf_score + score.rhyme_score) / 2
        for i, artist in enumerate(cls.ARTISTS):
            if avg < (artist[0].tfidf_score_avg+artist[0].rhyme_score_avg)/2:
                extended_artists.append(artist)
            else:
                extended_artists.append(None)
                extended_artists.extend(cls.ARTISTS[i:])
                break
        return extended_artists



