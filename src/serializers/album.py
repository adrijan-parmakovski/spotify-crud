from ._base import Serializer

from ..models.album import Album, Copyright
from ..models.simplified_album import SimplifiedAlbum
from .artist import SimplifiedArtistSerializer
from .common import _ImageSerializer, _RestrictionSerializer


class _Copyright(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Copyright:
        return Copyright(text=input["text"], type=input["type"])

    @staticmethod
    def serialize(input: Copyright) -> dict:
        return {"text": input.text, "type": input.type}


class SimplifiedAlbumSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> SimplifiedAlbum:
        return SimplifiedAlbum(
            album_group=input.get("album_group"),
            album_type=input["album_type"],
            artists=[
                SimplifiedArtistSerializer.deserialize(artist)
                for artist in input["artists"]
            ],
            available_markets=input.get("available_markets", []),
            external_urls=input["external_urls"],
            href=input["href"],
            id=input["id"],
            images=[_ImageSerializer.deserialize(image) for image in input["images"]],
            name=input["name"],
            release_date=input["release_date"],
            release_date_precision=input["release_date_precision"],
            restrictions=[
                _RestrictionSerializer.deserialize(res) for res in input["restrictions"]
            ],
            total_tracks=input["total_tracks"],
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: SimplifiedAlbum) -> dict:
        return {
            "album_group": input.album_group if input.album_group else None,
            "album_type": input.album_type,
            "artists": [
                SimplifiedArtistSerializer.serialize(artist) for artist in input.artists
            ],
            "available_markets": input.available_markets
            if input.available_markets
            else [],
            "external_urls": input.external_urls,
            "href": input.href,
            "id": input.id,
            "images": [_ImageSerializer.serialize(image) for image in input.images],
            "name": input.name,
            "release_date": input.release_date,
            "release_date_precision": input.release_date_precision,
            "restrictions": [
                _RestrictionSerializer.serialize(res) for res in input.restrictions
            ],
            "total_tracks": input.total_tracks,
            "type": input.type,
            "uri": input.uri,
        }


class AlbumSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Album:
        pass

    @staticmethod
    def serialize(input: Album) -> dict:
        pass
