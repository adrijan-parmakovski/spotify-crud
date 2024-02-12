from dataclasses import dataclass


@dataclass
class Image:
    height: int
    url: str
    width: int
