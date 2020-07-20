from .models import Artist

class Artists:
    artist_names = [
        "Madonna",
        "Michael Jackson",
        "Eminem",
        "2Pac",
        "Led Zeppelin",
        "Queen",
        "Aretha Franklin",
        "Dolly Parton"
    ]
    artist_genres = [
        "pop",
        "pop",
        "rap",
        "rap",
        "rock",
        "rock",
        "r-n-b",
        "country"
    ]
    artist_objects = [Artist.objects.get(name=name) for name in artist_names]

    ARTISTS = list(zip(artist_objects, artist_genres))
    ARTISTS = sorted(ARTISTS, key=lambda o: (o[0].tfidf_score_avg + o[0].rhyme_score_avg)/2, reverse=True)

    @classmethod
    def add_artist(cls, score):
        extended_artists = []
        avg = (score.tfidf_score + score.rhyme_score) / 2
        added_new = False
        for i, artist in enumerate(cls.ARTISTS):
            if avg < (artist[0].tfidf_score_avg+artist[0].rhyme_score_avg)/2:
                extended_artists.append(artist)
            else:
                extended_artists.append(None)
                added_new = True
                extended_artists.extend(cls.ARTISTS[i:])
                break
                
        # if new score hasn't been added yet, add it at the end
        if not added_new:
            extended_artists.append(None)

        return extended_artists



