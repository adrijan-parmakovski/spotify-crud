from src.utils.configs import SPOTIFY_CONFIGS
import json

from src.controllers.client import SpotifyClient, SpotifyApiRequests
from src.controllers.request_processor import AsyncRequestHandler
from src.serializers.artist import SpotifyArtistSerializer
from aiohttp import ClientSession

from asyncio import run


# def foo():
# print(SPOTIFY_CONFIGS.__dict__)
# print(SPOTIFY_CONFIGS.base_64_secret)
# client = SpotifyClient()
# tracks = client.get_saved_tracks()
# print(tracks[0])
# with open("tracks.json", "w") as f:
# json.dump(tracks, f)
# with open("tracks.json", "r") as f:
# tracks = json.load(f)
# print(tracks[0])

API = SpotifyApiRequests(
    base_url=SPOTIFY_CONFIGS.spotify_web_api_url,
    client_id=SPOTIFY_CONFIGS.client_id,
    client_secret=SPOTIFY_CONFIGS.client_secret,
    refresh_token=SPOTIFY_CONFIGS.refresh_token,
)


async def foo():
    # r_dict = {"method": "GET", "url": "http://google.com"}
    session = ClientSession()
    c = AsyncRequestHandler(session)
    client = SpotifyClient(api_requests=API, request_processor=c)
    """
    json_data = await client.get_artist(artist_id="3q7HBObVc0L8jNeTe5Gofh")
    with open("sample_artist.json", "w") as f:
        json.dump(json_data, f, indent=4)
    artist = SpotifyArtistSerializer.deserialize(json_data)
    print(artist)
    await session.close()
    """
    tracks = client.get_saved_tracks()
    print(tracks)


def serializer_test():
    with open("sample_track.json", "r") as f:
        _raw_data = json.loads(f.read())
    artist = SpotifyArtistSerializer.deserialize(_raw_data["track"]["artists"][0])
    print(artist)


# run(foo())
serializer_test()
