from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProfileDataClass:
    name: str
    surname: str
    age: int


@dataclass
class UserDataClass:
    id: int
    email: str
    password: str
    is_superuser: bool
    is_staff: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime
    profile: ProfileDataClass
