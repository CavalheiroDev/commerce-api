from abc import abstractmethod
from datetime import datetime
from uuid import UUID


class Entity:
    def __init__(self, *args, **kwargs):
        pass

    id: UUID
    created: datetime
    modified: datetime

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()
