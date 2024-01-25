from importlib.metadata import requires
import requests
import json

from time import time

from ..utils.configs import SPOTIFY_CONFIGS


class SpotifyApi:
    def __init__(self) -> None:
        pass


class SpotifyClient:
    def __init__(self) -> None:
        self.refresh_token = SPOTIFY_CONFIGS.refresh_token
        self.account_id = SPOTIFY_CONFIGS.account_id
        self.access_token = None

    def _get_refresh_token(self, auth_code: str):
        headers = {
            "Authorization": "Basic " + SPOTIFY_CONFIGS.base64_secret,
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {
            "grant_type": "authorization_code",
            "code": SPOTIFY_CONFIGS.AUTH_CODE,
            "redirect_uri": SPOTIFY_CONFIGS.redirect_uri,
        }
        r = requests.post(SPOTIFY_CONFIGS.API_TOKEN_URL, headers=headers, data=data)
        self.refresh_token = r.json()["refresh_token"]

    def _get_access_token(self):
        r = requests.post(
            url=SPOTIFY_CONFIGS.api_token_url,
            headers={"Authorization": "Basic {}".format(SPOTIFY_CONFIGS.base64_secret)},
            data={
                "grant_type": "refresh_token",
                "refresh_token": SPOTIFY_CONFIGS.refresh_token,
            },
        )
        if "error" in r.json().keys():
            print(r.json())
            raise Exception(r.json()["error"])
        else:
            self.access_token = r.json()["access_token"]
            self.expires_at = int(time()) + 3550

    def connect(self):
        if not self.access_token or self.expires_at - int(time()) < 300:
            self._get_access_token()
        pass

    def get_saved_tracks(self):
        self.connect()

        tracks = []

        url = "https://api.spotify.com/v1/me/tracks"
        while True:
            r = requests.get(
                url=url,
                headers={
                    "Authorization": "Bearer {}".format(self.access_token),
                    "Content-Type": "application-json",
                },
                params={"limit": 50},
            )
            print("Running url: {}".format(url))
            tracks.extend(r.json()["items"])

            if r.json().get("next") is not None:
                url = r.json()["next"]
            else:
                break
        return tracks

    def get_object(self, endpoint):
        self.connect()

        url = f"{SPOTIFY_CONFIGS.spotify_web_api_url}/{SpotifyConfigs.spotify_web_api_version}/{endpoint}"

        r = requests.get(
            url=url,
            headers={
                "Authorization": "Bearer {}".format(self.access_token),
                "Content-Type": "application-json",
            },
        )
        return r.json()
