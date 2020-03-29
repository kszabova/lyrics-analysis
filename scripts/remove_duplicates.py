import ijson
import json

# removing duplicates is based on the assumption that songs by one
# artist are stored next to each other
with open("../data/song_lyrics_english_only.json") as file:
    objects = ijson.items(file, "item")

    with open("../data/song_lyrics_no_duplicates.json", 'w') as out_file:
        out_file.write("[\n")

        prev_artist_id = None
        prev_title = None
        duplicates = 0

        for object in objects:

            if object["rg_artist_id"] == prev_artist_id and object["title"] == prev_title:
                # we have a duplicate, do nothing
                duplicates += 1
            else:
                # keep the object
                out_file.write(json.dumps(object))
                out_file.write(",\n")
                prev_artist_id = object["rg_artist_id"]
                prev_title = object["title"]

        out_file.write("]")
        print(duplicates)
