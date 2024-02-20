from ._base import Serializer
from ..models.artist import Artist, Followers
from ..models.simplified_artist import SimplifiedArtist
from .common import _ImageSerializer, _ExternalUrlSerializer


class ArtistSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Artist:
        return Artist(
            external_urls=_ExternalUrlSerializer.deserialize(input["external_urls"]),
            followers=_ArtistFollowerSerializer.deserialize(input["followers"]),
            genres=input.get("genres", []),
            href=input["href"],
            id=input["id"],
            images=[_ImageSerializer.deserialize(i) for i in input["images"]],
            name=input["name"],
            popularity=input["popularity"],
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: Artist) -> dict:
        return {
            "external_urls": _ExternalUrlSerializer.serialize(input.external_urls),
            "followers": _ArtistFollowerSerializer.serialize(input.followers),
            "genres": input.genres,
            "href": input.href,
            "id": input.id,
            "images": [_ImageSerializer.serialize(i) for i in input.images],
            "name": input.name,
            "popularity": input.popularity,
            "type": input.type,
            "uri": input.uri,
        }


class SimplifiedArtistSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> SimplifiedArtist:
        return SimplifiedArtist(
            external_urls=_ExternalUrlSerializer.deserialize(input["external_urls"]),
            href=input["href"],
            id=input["id"],
            name=input["name"],
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: SimplifiedArtist) -> dict:
        return {
            "external_urls": _ExternalUrlSerializer.serialize(input.external_urls),
            "href": input.href,
            "id": input.id,
            "name": input.name,
            "type": input.type,
            "uri": input.uri,
        }


class _ArtistFollowerSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Followers:
        return Followers(href=input["href"], total=input["total"])

    @staticmethod
    def serialize(input: Followers) -> dict:
        return {"href": input.href, "total": input.total}
