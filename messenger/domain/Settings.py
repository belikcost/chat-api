from abc import ABC
from datetime import tzinfo


class Settings(ABC):
    id: int
    name: str
    timezone: tzinfo
