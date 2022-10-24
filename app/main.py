from spotify_crud.client import SpotifyClient

import json


if __name__ == '__main__':
    client = SpotifyClient()
    tracks = client.get_object(url="https://api.spotify.com/v1/artists/0lAWpj5szCSwM4rUMHYmrr")

    # with open('sample.json', 'w') as f:
    #     json.dump(tracks[:1], f)

    with open('artist_sample.json', 'w') as f:
        json.dump(tracks, f)
