from dataclasses import dataclass
from base64 import b64encode
import os


@dataclass(frozen=True)
class SpotifyConfigs:
    # credentials
    account_id = os.environ["SPOTIFY__ACCOUNT_ID"]
    client_id = os.environ["SPOTIFY__CLIENT_ID"]
    client_secret = os.environ["SPOTIFY__CLIENT_SECRET"]
    refresh_token = os.environ["SPOTIFY__REFRESH_TOKEN"]
    base_64_secret = b64encode(
        "{}:{}".format(client_id, client_secret).encode()
    ).decode()
    # scope and URI
    scopes = "user-library-read user-library-modify"
    redirect_uri = "http://google.com"
    # URLs
    api_token_url = "https://accounts.spotify.com/api/token"
    spotify_web_api_url = "https://api.spotify.com"
    spotify_web_api_version = "v1"


SPOTIFY_CONFIGS = SpotifyConfigs()
