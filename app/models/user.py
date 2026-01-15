from typing import Optional
from datetime import datetime


class User:
    def __init__(
        self,
        id: str,
        username: str,
        email: str,
        hashed_password: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at
        self.updated_at = updated_at
