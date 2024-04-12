import asyncio
import requests
from src.utils.configs import SPOTIFY_CONFIGS
import json

import logging

from src.models.configs import SpotifyConfigs
from src.controllers.client import SpotifyClient, SpotifyApiRequests
from src.controllers.request_processor import AsyncProcessor

from asyncio import run

logger = logging.getLogger(__file__)


API = SpotifyApiRequests(
    base_url=SPOTIFY_CONFIGS.spotify_web_api_url,
    client_id=SPOTIFY_CONFIGS.client_id,
    client_secret=SPOTIFY_CONFIGS.client_secret,
    refresh_token=SPOTIFY_CONFIGS.refresh_token,
)


async def get_saved_tracks(configs: SpotifyConfigs = SPOTIFY_CONFIGS):
    # generate the API and the client
    api = SpotifyApiRequests(
        base_url=configs.spotify_web_api_url,
        client_id=configs.client_id,
        client_secret=configs.client_secret,
        refresh_token=configs.refresh_token,
    )
    async with AsyncProcessor() as request_processor:
        client = SpotifyClient(api_requests=api, request_processor=request_processor)
        headers = client.headers
        await client.get_saved_tracks()
        return None
        # get tracks
        url = "https://api.spotify.com/v1/me/tracks"
        # send request
        r = requests.get(url, headers=headers, params={"limit": 1})
        data = r.json()
        print(f"There are a total of {data['total']} saved tracks.")

        _requests = _generate_saved_tracks_requests(url, headers, data["total"])
        tasks = []
        for request in _requests:
            tasks.append(
                asyncio.ensure_future(request_processor.submit_request(request))
            )
        data = await asyncio.gather(*tasks)
        print(f"{len(data)} tracks returned.")


def _generate_saved_tracks_requests(
    url: str, headers: dict, total_tracks: int
) -> list[dict]:
    # empty list for generating all the requests
    requests = []
    # generate requests for all tracks
    offset = 0
    # iterate until we reach the end of the tracks
    while offset < total_tracks:
        request = {
            "method": "GET",
            "url": url,
            "headers": headers,
            "params": {"limit": 50, "offset": offset},
        }
        requests.append(request)
        offset += 50
    with open("requests.json", "w") as f:
        json.dump(requests, f, indent=4)
    return requests
