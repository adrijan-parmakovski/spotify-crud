from dataclasses import dataclass
from .common import ExternalUrl


@dataclass
class SimplifiedArtist:
    external_urls: ExternalUrl
    href: str
    id: str
    name: str
    type: str
    uri: str
