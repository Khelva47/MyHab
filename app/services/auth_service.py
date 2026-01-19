from typing import Optional
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import verify_password, get_password_hash
from app.schemas.user import UserCreate


class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_create: UserCreate) -> User:

        now = datetime.now(timezone.utc)

        # Hash the password before storing
        hashed_password = get_password_hash(user_create.password)
        
        user = User(
            id=user_create.id,
            username=user_create.username,
            email=user_create.email,
            hashed_password=hashed_password,
            created_at=now,
            updated_at=now
        )

        # Adding user to the database
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()
    
    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user