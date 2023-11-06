from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDataclass:
    id: int
    email: str
    password: str
    is_superuser: bool
    is_staff: bool
    is_active: bool
    last_login: str
    created_at: datetime
    updated_at: datetime
