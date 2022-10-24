import json

from spotify_crud.client import SpotifyClient


def get_saved_tracks():
    client = SpotifyClient()

    tracks = client.get_saved_tracks()
    
    