from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ExternalUrls:
    spotify: str


@dataclass
class ArtistFollowers:
    href: str
    total: int


@dataclass
class Image:
    height: int
    url: str
    width: int


@dataclass
class SpotifyArtist:
    external_urls: ExternalUrls
    followers: ArtistFollowers | None
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    name: str
    popularity: float | None
    type: str
    uri: str
