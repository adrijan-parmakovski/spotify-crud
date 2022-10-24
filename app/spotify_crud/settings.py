from dataclasses import dataclass
from base64 import b64encode
import os


@dataclass(frozen=True)
class SpotifyConfigs:
    ACCOUNT_ID = os.environ['ACCOUNT_ID']
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    SCOPES = 'user-library-read user-library-modify'
    REDIRECT_URI = 'http://google.com/'
    REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
    BASE64_SECRET = b64encode('{}:{}'.format(CLIENT_ID, CLIENT_SECRET).encode()).decode()
    # URLs
    API_TOKEN_URL = 'https://accounts.spotify.com/api/token'
