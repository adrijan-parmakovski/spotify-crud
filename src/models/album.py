from dataclasses import dataclass

from .common import ExternalUrl, Image, Restriction, ExternalIds
from .artist import Artist
from .simplified_track import SimplifiedTrack

from typing import List


@dataclass
class Copyright:
    text: str
    type: str


@dataclass
class Album:
    album_type: str
    artists: List[Artist]
    available_markets: List[str]
    copyrights: List[Copyright]
    external_ids: ExternalIds
    external_urls: ExternalUrl
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    label: str
    name: str
    popularity: float | None
    release_date: str
    restrictions: List[Restriction]
    total_tracks: int
    tracks: List[SimplifiedTrack]
    type: str
    uri: str
