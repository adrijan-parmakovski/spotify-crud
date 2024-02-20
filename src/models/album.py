from dataclasses import dataclass

from ..models.common import ExternalUrl
from .common import Image
from .artist import Artist
from .simplified_track import SimplifiedTrack

from typing import List


@dataclass
class Copyright:
    text: str
    type: str


@dataclass
class ExternalIds:
    isrc: str
    ean: str
    upc: str


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
    images: List[str]
    label: str
    name: str
    popularity: float | None
    release_date: str
    restrictions: List[Restriction]
    total_tracks: int
    tracks: List[SimplifiedTrack]
    type: str
    uri: str
