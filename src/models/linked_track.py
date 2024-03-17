from dataclasses import dataclass

from .common import ExternalUrl


@dataclass
class LinkedTrack:
    external_urls: ExternalUrl
    href: str
    id: str
    type: str
    uri: str
