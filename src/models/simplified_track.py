from dataclasses import dataclass
from typing import List
from models.common import ExternalUrl, Restriction
from models.linked_track import LinkedTrack

from models.simplified_artist import SimplifiedArtist


@dataclass
class SimplifiedTrack:
    artists: List[SimplifiedArtist]
    available_markets: List[str] | None
    disc_number: int
    duration_ms: int
    explicit: bool
    externa_urls: ExternalUrl
    href: str
    id: str
    is_local: bool
    is_playable: bool | None
    linked_from: LinkedTrack | None
    name: str
    preview_url: str
    restrictions: List[Restriction]
    track_number: int
    type: str
    uri: str
