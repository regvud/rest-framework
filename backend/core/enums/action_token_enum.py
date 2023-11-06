from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        "activate",
        timedelta(minutes=30),
    )

    RECOVERY = (
        "recover",
        timedelta(minutes=10),
    )

    SOCKET = (
        "socket",
        timedelta(seconds=5),
    )

    def __init__(self, token_type, lifetime) -> None:
        self.token_type = token_type
        self.lifetime = lifetime
