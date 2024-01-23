from src.utils.configs import SPOTIFY_CONFIGS
from src.controllers.client import SpotifyClient
import json


def foo():
    # print(SPOTIFY_CONFIGS.__dict__)
    # print(SPOTIFY_CONFIGS.base_64_secret)
    # client = SpotifyClient()
    # tracks = client.get_saved_tracks()
    # print(tracks[0])
    # with open("tracks.json", "w") as f:
    # json.dump(tracks, f)
    with open("tracks.json", "r") as f:
        tracks = json.load(f)
    print(tracks[0])


foo()
