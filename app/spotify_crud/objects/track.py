from dataclasses import dataclass
from dataclass import dataclass
from datetime import datetime

from typing import List, Dict


@dataclass
class SavedTrack():
    id: str
    added_at: str


@dataclass
class Track():
    id: str
    album_id: str
    album_artists: List[Dict[str, str]]
    track_artists: List[Dict[str, str]]
    type: str
    duration: int
    
