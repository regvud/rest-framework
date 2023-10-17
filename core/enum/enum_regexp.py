from enum import Enum


class RegExp(Enum):
    PROFILE = (
        r'^[A-Z][a-zA-Z]{1,20}$',
        'First letter uppercase, no digits, min 2 max 20 chars'
    )
    PASSWORD = (
        r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,128}$',
        'Password length 8-128 characters, at least one letter and one number'
    )

    def __init__(self, pattern, msg):
        self.msg = msg
        self.pattern = pattern
