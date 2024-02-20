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
    followers: Followers
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    name: str
    popularity: float
    type: str
    uri: str
