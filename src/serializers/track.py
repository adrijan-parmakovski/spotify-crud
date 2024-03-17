from ..models.track import Track
from ..models.linked_track import LinkedTrack

from ._base import Serializer
from .artist import ArtistSerializer
from .album import SimplifiedAlbumSerializer
from .common import (
    _ExternalUrlSerializer,
    _ExternalIdsSerializer,
    _RestrictionSerializer,
)


class TrackSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Track:
        return Track(
            album=SimplifiedAlbumSerializer.deserialize(input["album"]),
            artists=[
                ArtistSerializer.deserialize(artist) for artist in input["artists"]
            ],
            available_markets=input.get("available_markets", []),
            disc_number=input["disc_number"],
            duration_ms=input["duration_ms"],
            explicit=input["explicit"],
            external_ids=_ExternalIdsSerializer.deserialize(input["external_ids"]),
            external_urls=_ExternalUrlSerializer.deserialize(input["external_urls"]),
            href=input["href"],
            id=input["id"],
            is_local=input["is_local"],
            is_playable=input.get("is_playable"),
            linked_from=_LinkedTrackSerializer.deserialize(input["linked_from"]),
            name=input["name"],
            popularity=input["popularity"],
            preview_url=input["preview_url"],
            restrictions=[
                _RestrictionSerializer.deserialize(r) for r in input["restrictions"]
            ],
            track_number=input["track_number"],
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: Track) -> dict:
        return {
            "album": SimplifiedAlbumSerializer.serialize(input.album),
            "artists": [ArtistSerializer.serialize(artist) for artist in input.artists],
            "available_markets": input.available_markets
            if input.available_markets
            else [],
            "disc_number": input.disc_number,
            "duration_ms": input.duration_ms,
            "explicit": input.explicit,
            "external_ids": _ExternalIdsSerializer.serialize(input.external_ids),
            "external_urls": _ExternalUrlSerializer.serialize(input.external_urls),
            "href": input.href,
            "id": input.id,
            "is_local": input.is_local,
            "is_playable": input.is_playable,
            "linked_from": _LinkedTrackSerializer.serialize(input.linked_from),
            "name": input.name,
            "popularity": input.popularity,
            "preview_url": input.preview_url,
            "restrictions": [
                _RestrictionSerializer.serialize(r) for r in input.restrictions
            ],
            "track_number": input.track_number,
            "type": input.type,
            "uri": input.uri,
        }


class _LinkedTrackSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> LinkedTrack:
        return LinkedTrack(
            external_urls=_ExternalUrlSerializer.deserialize(input["external_urls"]),
            href=input["href"],
            id=input["id"],
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: LinkedTrack) -> dict:
        return {
            "external_urls": input.external_urls,
            "href": input.href,
            "id": input.id,
            "type": input.type,
            "uri": input.uri,
        }
