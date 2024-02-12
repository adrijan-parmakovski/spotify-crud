from ._base import Serializer

from src.models.common import Image, ExternalUrl


class _ImageSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Image:
        return Image(url=input["url"], height=input["height"], width=input["width"])

    @staticmethod
    def serialize(input: Image) -> dict:
        return {"url": input.url, "height": input.height, "width": input.width}


class _ExternalUrlSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> ExternalUrl:
        return ExternalUrl(spotify=input["spotify"])

    @staticmethod
    def serialize(input: ExternalUrl) -> dict:
        return {"spotify": input.spotify}
