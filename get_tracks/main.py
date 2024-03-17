from requests import session
from src.utils.configs import SPOTIFY_CONFIGS
import json

import logging

from src.models.configs import SpotifyConfigs
from src.controllers.client import SpotifyClient, SpotifyApiRequests
from src.controllers.request_processor import AsyncRequestHandler
from src.serializers.track import TrackSerializer
from aiohttp import ClientSession

from asyncio import run

logger = logging.getLogger(__file__)


API = SpotifyApiRequests(
    base_url=SPOTIFY_CONFIGS.spotify_web_api_url,
    client_id=SPOTIFY_CONFIGS.client_id,
    client_secret=SPOTIFY_CONFIGS.client_secret,
    refresh_token=SPOTIFY_CONFIGS.refresh_token,
)


def get_saved_tracks(configs: SpotifyConfigs = SPOTIFY_CONFIGS):
    # generate the API and the client
    api = SpotifyApiRequests(
        base_url=configs.spotify_web_api_url,
        client_id=configs.client_id,
        client_secret=configs.client_secret,
        refresh_token=configs.refresh_token,
    )
    client = SpotifyClient(
        api_requests=api, request_processor=AsyncRequestHandler(session=ClientSession())
    )
    # get tracks
    raw_tracks = client.get_saved_tracks()
    logger.info(f"Returned {len(raw_tracks)} saved tracks.")
    # serialize tracks
    tracks = [TrackSerializer.deserialize(track) for track in raw_tracks]
    logger.info(tracks[0])
