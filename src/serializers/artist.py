from ._base import Serializer
from ..models.artist import Image, SpotifyArtist, ArtistFollowers, ExternalUrls


class SpotifyArtistSerializer:
    @staticmethod
    def deserialize(input: dict) -> SpotifyArtist:
        return SpotifyArtist(
            external_urls=_ExternalUrlsSerializer.deserialize(input["external_urls"])
            if input.get("external_urls")
            else None,
            followers=_ArtistFollowersSerializer.deserialize(input["followers"])
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
    def serialize(input: SpotifyArtist) -> dict:
        return {
            "external_urls": _ExternalUrlsSerializer.serialize(input.external_urls),
            "followers": _ArtistFollowersSerializer.serialize(input.followers)
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


class _ArtistFollowersSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> ArtistFollowers:
        return ArtistFollowers(href=input["href"], total=input["total"])

    @staticmethod
    def serialize(input: ArtistFollowers) -> dict:
        return {"href": input.href, "total": input.total}


class _ExternalUrlsSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> ExternalUrls:
        return ExternalUrls(spotify=input["spotify"])

    @staticmethod
    def serialize(input: ExternalUrls) -> dict:
        return {"spotify": input.spotify}


class _ImageSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Image:
        return Image(url=input["url"], height=input["height"], width=input["width"])

    @staticmethod
    def serialize(input: Image) -> dict:
        return {"url": input.url, "height": input.height, "width": input.width}
