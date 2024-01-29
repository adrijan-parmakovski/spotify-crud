from dataclasses import dataclass, field

from typing import List, Dict


@dataclass
class SpotifyTrack:
    pass


@dataclass
class ExternalUrls:
    spotify: str


@dataclass
class Image:
    height: int
    url: str
    width: int


@dataclass
class ArtistFollowers:
    href: str
    total: int
