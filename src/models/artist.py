from dataclasses import dataclass, field
from typing import List, Dict

from .common import Image, ExternalUrl


@dataclass
class Followers:
    href: str
    total: int


@dataclass
class Artist:
    external_urls: ExternalUrl
    followers: Followers | None
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    name: str
    popularity: float | None
    type: str
    uri: str


@dataclass
class SimplifiedArtist:
    external_urls: ExternalUrl
    href: str
    id: str
    name: str
    type: str
    uri: str
