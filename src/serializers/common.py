from ._base import Serializer

from src.models.common import Image


class _ImageSerializer(Serializer):
    @staticmethod
    def deserialize(input: dict) -> Image:
        return Image(url=input["url"], height=input["height"], width=input["width"])

    @staticmethod
    def serialize(input: Image) -> dict:
        return {"url": input.url, "height": input.height, "width": input.width}
