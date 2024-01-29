from dataclasses import dataclass
from base64 import b64encode
import os

from src.models.configs import SpotifyConfigs


SPOTIFY_CONFIGS = SpotifyConfigs(
    account_id=os.environ["SPOTIFY__ACCOUNT_ID"],
    client_id=os.environ["SPOTIFY__CLIENT_ID"],
    client_secret=os.environ["SPOTIFY__CLIENT_SECRET"],
    refresh_token=os.environ["SPOTIFY__REFRESH_TOKEN"],
    # scope and URI
    scopes="user-library-read user-library-modify",
    redirect_uri="http://google.com",
    # URLs
    api_token_base_url="https://accounts.spotify.com",
    api_token_endpoint="api/token",
    spotify_web_api_url="https://api.spotify.com",
    spotify_web_api_version="v1",
)
