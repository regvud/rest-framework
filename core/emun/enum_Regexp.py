from enum import Enum


class RegExp(Enum):
    DEFAULT = (
        r'^[A-Z][a-zA-Z\d]{1,20}$',
        'First letter must be uppercase, 1-20 symbols overall length'
    )

    def __init__(self, pattern, msg):
        self.pattern = pattern
        self.msg = msg
