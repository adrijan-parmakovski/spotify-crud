from dataclasses import dataclass

from .common import Image
from .artist import Artist


@dataclass
class SpotifyAlbum:
    pass


@dataclass
class Restrictions:
    reason: str


@dataclass
class Copyrights:
    text: str
    type: str


@dataclass
class ExternalIds:
    isrc: str
    ean: str
    upc: str
