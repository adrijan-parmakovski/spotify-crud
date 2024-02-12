from ._base import Serializer
from ..models.artist import Image, Artist, Followers, ExternalUrl, SimplifiedArtist
from .common import _ImageSerializer, _ExternalUrlSerializer


class ArtistSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Artist:
        return Artist(
            external_urls=_ExternalUrlSerializer.deserialize(input["external_urls"])
            if input.get("external_urls")
            else None,
            followers=_ArtistFollowerSerializer.deserialize(input["followers"])
            if input.get("followers")
            else None,
            genres=input.get("genres", []),
            href=input["href"],
            id=input["id"],
            images=[_ImageSerializer.deserialize(i) for i in input["images"]]
            if input.get("images")
            else [],
            name=input["name"],
            popularity=input.get("popularity"),
            type=input["type"],
            uri=input["uri"],
        )

    @staticmethod
    def serialize(input: Artist) -> dict:
        return {
            "external_urls": _ExternalUrlSerializer.serialize(input.external_urls),
            "followers": _ArtistFollowerSerializer.serialize(input.followers)
            if input.followers
            else None,
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
        pass

    @staticmethod
    def serialize(input: SimplifiedArtist) -> dict:
        pass


class _ArtistFollowerSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Followers:
        return Followers(href=input["href"], total=input["total"])

    @staticmethod
    def serialize(input: Followers) -> dict:
        return {"href": input.href, "total": input.total}


class _ImageSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Image:
        return Image(url=input["url"], height=input["height"], width=input["width"])

    @staticmethod
    def serialize(input: Image) -> dict:
        return {"url": input.url, "height": input.height, "width": input.width}
