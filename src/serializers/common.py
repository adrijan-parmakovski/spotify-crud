from ..models.common import Restriction
from ._base import Serializer

from src.models.common import Image, ExternalUrl, ExternalIds


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


class _RestrictionSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Restriction:
        return Restriction(reason=input["reason"])

    @staticmethod
    def serialize(input: Restriction) -> dict:
        return {"reason": input.reason}


class _ExternalIdsSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> ExternalIds:
        return ExternalIds(isrc=input["isrc"], ean=input["ean"], upc=input["upc"])

    @staticmethod
    def serialize(input: ExternalIds) -> dict:
        return {"isrc": input.isrc, "ean": input.ean, "upc": input.upc}
