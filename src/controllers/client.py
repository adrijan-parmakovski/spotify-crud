from importlib.metadata import requires
import requests
import json
from typing import Dict
from asyncio import run
from time import time
from datetime import datetime, timedelta
from base64 import b64encode

from .request_processor import AsyncRequestHandler

from ..utils.configs import SPOTIFY_CONFIGS

API_VERSION = SPOTIFY_CONFIGS.spotify_web_api_version


class SpotifyApiRequests:
    def __init__(
        self, base_url: str, client_id: str, client_secret: str, refresh_token: str
    ) -> None:
        self._base_url = base_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._refresh_token = refresh_token

    @property
    def base64_secret(self) -> str:
        return b64encode(
            "{}:{}".format(self._client_id, self._client_secret).encode()
        ).decode()

    def _create_request(
        self,
        method: str,
        endpoint: str,
        headers: Dict[str, str],
        url: str = SPOTIFY_CONFIGS.spotify_web_api_url,
        params: Dict[str, str] | None = None,
        data: Dict[str, str] | None = None,
        add_api_version: bool = True,
    ) -> Dict[str, str | Dict[str, str]]:
        # generate the URL based on the base URL, endpoint and version
        url = "{}{}/{}".format(
            url, f"/{API_VERSION}" if add_api_version else "", endpoint
        )
        request = {
            "method": method,
            "url": url,
            "headers": headers,
        }
        # add payload if necessary
        if data:
            request["data"] = data
        # add parameters if necessary
        if params:
            request["params"] = params
        return request

    def get_access_token(self) -> dict:
        return self._create_request(
            method="POST",
            url=SPOTIFY_CONFIGS.api_token_base_url,
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic {}".format(self.base64_secret),
            },
            add_api_version=False,
            endpoint=SPOTIFY_CONFIGS.api_token_endpoint,
            data={
                "grant_type": "refresh_token",
                "refresh_token": self._refresh_token,
                "client_id": self._client_id,
            },
        )

    def get_sample_tracks(self, headers: Dict[str, str]) -> dict:
        return self._create_request(
            method="GET",
            url=SPOTIFY_CONFIGS.spotify_web_api_url,
            endpoint="me/tracks",
            headers=headers,
        )


class SpotifyClient:
    def __init__(
        self, api_requests: SpotifyApiRequests, request_processor: AsyncRequestHandler
    ) -> None:
        self._api = api_requests
        self._request_processor = request_processor
        self._access_token: str | None = None
        self._access_token_expires_at: datetime | None = None

    @property
    def headers(self) -> Dict[str, str]:
        if not self._access_token:
            self._get_access_token()
        if datetime.now() > self._access_token_expires_at:
            self._get_access_token()
        return {
            "Content-Type": "application-json",
            "Authorization": "Bearer {}".format(self._access_token),
        }

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
        request = self._api.get_access_token()
        response = requests.request(
            method=request["method"],
            url=request["url"],
            headers=request["headers"],
            data=request["data"],
        )
        if response.status_code == 200:
            self._access_token = response.json()["access_token"]
            self._access_token_expires_at = datetime.now() + timedelta(seconds=3550)
            return response.status_code
        if response.status_code != 200:
            print(request["headers"])
            print(response.text)
        # r = requests.post(:with expression as target:
        # pass
        #     url=SPOTIFY_CONFIGS.api_token_base_url,
        #     headers={"Authorization": "Basic {}".format(SPOTIFY_CONFIGS.base64_secret)},
        #     data={
        #         "grant_type": "refresh_token",
        #         "refresh_token": SPOTIFY_CONFIGS.refresh_token,
        #     },
        # )
        # if "error" in r.json().keys():
        # print(r.json())
        # raise Exception(r.json()["error"])
        # else:
        # self.access_token = r.json()["access_token"]
        # self.expires_at = int(time()) + 3550

    async def get_sample_tracks(self):
        request = self._api.get_sample_tracks(self.headers)
        json_data, headers, status_code = await self._request_processor.send_request(
            request
        )
        return json_data["items"]

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
