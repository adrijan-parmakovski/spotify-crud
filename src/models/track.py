from dataclasses import dataclass

from typing import List

from .common import ExternalIds, ExternalUrl, Restriction
from .artist import Artist
from .simplified_album import SimplifiedAlbum
from .linked_track import LinkedTrack


@dataclass
class Track:
    album: SimplifiedAlbum
    artists: List[Artist]
    available_markets: List[str] | None
    disc_number: int
    duration_ms: int
    explicit: bool
    external_ids: ExternalIds
    external_urls: ExternalUrl
    href: str
    id: str
    is_local: bool
    is_playable: bool | None
    linked_from: LinkedTrack
    name: str
    popularity: float
    preview_url: str
    restrictions: List[Restriction]
    track_number: int
    type: str
    uri: str
