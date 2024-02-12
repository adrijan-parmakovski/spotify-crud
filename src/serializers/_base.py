from abc import ABC
from typing import Any


class Serializer(ABC):
    def deserialize(self, input: dict) -> Any:
        pass

    def serialize(self, input: Any) -> dict:
        pass
