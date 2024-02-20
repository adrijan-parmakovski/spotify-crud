from dataclasses import dataclass
from typing import List

from .common import ExternalUrl, Image, Restriction
from .simplified_artist import SimplifiedArtist


@dataclass
class SimplifiedAlbum:
    album_group: str | None
    album_type: str
    artists: List[SimplifiedArtist]
    available_markets: List[str] | None
    external_urls: ExternalUrl
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    restrictions: List[Restriction]
    total_tracks: int
    type: str
    uri: str
