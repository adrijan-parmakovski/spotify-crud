from dataclasses import dataclass
from base64 import b64encode


@dataclass
class SpotifyConfigs:
    account_id: str
    client_id: str
    client_secret: str
    refresh_token: str
    scopes: str
    redirect_uri: str
    api_token_base_url: str
    api_token_endpoint: str
    spotify_web_api_url: str
    spotify_web_api_version: str

    def __post_init__(self):
        self.base64_secret = b64encode(
            "{}:{}".format(self.client_id, self.client_secret).encode()
        ).decode()
