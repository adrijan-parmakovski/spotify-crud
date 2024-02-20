from dataclasses import dataclass


@dataclass
class Image:
    height: int
    url: str
    width: int


@dataclass
class Restriction:
    reason: str


@dataclass
class ExternalIds:
    isrc: str
    ean: str
    upc: str


@dataclass
class ExternalUrl:
    spotify: str
