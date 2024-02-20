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
class ExternalUrl:
    spotify: str
