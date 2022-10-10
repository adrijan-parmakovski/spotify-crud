import json
import requests

from time import time

from settings import SpotifyConfigs


class SpotifyClient():
    def __init__(self) -> None:
        self.refresh_token = SpotifyConfigs.REFRESH_TOKEN
        self.account_id = SpotifyConfigs.ACCOUNT_ID
        self.access_token = None

    def _get_refresh_token(self, auth_code: str):
        headers = {
            'Authorization': 'Basic ' + SpotifyConfigs.BASE64_SECRET,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'authorization_code',
            'code': SpotifyConfigs.AUTH_CODE,
            'redirect_uri': SpotifyConfigs.REDIRECT_URI
        }
        r = requests.post(SpotifyConfigs.API_TOKEN_URL, headers=headers, data=data)
        self.refresh_token = r.json()['refresh_token']

    def _get_access_token(self):
        r = requests.post(url=SpotifyConfigs.API_TOKEN_URL,
                          headers={'Authorization': 'Basic {}'.format(SpotifyConfigs.BASE64_SECRET)},
                          data={
                            'grant_type': 'refresh_token',
                            'refresh_token': SpotifyConfigs.REFRESH_TOKEN
                          })
        self.access_token = r.json()['access_token']
        self.expires_at = int(time()) + 3550

    def connect(self):
        if not self.access_token or self.expires_at - int(time()) < 300:
            self._get_access_token()
        pass

    def get_saved_tracks(self):
        self.connect()

        tracks = []

        url = 'https://api.spotify.com/v1/me/tracks'
        while True:
            r = requests.get(url=url,
                                headers={
                                'Authorization': 'Bearer {}'.format(self.access_token),
                                'Content-Type': 'application-json'
                                },
                            params={'limit': 50}
                            )
            print('Running url: {}'.format(url))
            tracks.extend(r.json()['items'])

            if r.json().get('next') is not None:
                url = r.json()['next']
            else:
                break
        return tracks


if __name__ == '__main__':
    client = SpotifyClient()
    # client.connect()
    # print(client.access_token)
    tracks = client.get_saved_tracks()
    print(len(tracks))
