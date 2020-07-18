from .models import Artist, Song, Score

class Artists():
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
    sorted(ARTISTS, key=lambda o: o[0].tfidf_score_avg)

