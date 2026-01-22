from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from pwdlib import PasswordHash   # ← correct import
from app.core.config import Settings

# Recommended way: uses the best/default algorithm (Argon2 if installed, else bcrypt)
pwd_context = PasswordHash.recommended()

# Alternative 1: Explicitly force bcrypt (if you prefer it over Argon2)
# pwd_context = PasswordHash.with_algorithm("bcrypt")

# Alternative 2: No extras installed? It may fall back, but install [bcrypt] above
# pwd_context = PasswordHash()

# Optional: Enforce password length limit (bcrypt hard limit is 72 bytes UTF-8)
MAX_PASSWORD_BYTES = 72

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    if len(password.encode("utf-8")) > MAX_PASSWORD_BYTES:
        raise ValueError(
            f"Password too long: must be ≤ {MAX_PASSWORD_BYTES} bytes (UTF-8 encoded). "
            "Choose a shorter password or truncate manually if needed."
        )
    return pwd_context.hash(password)

# JWT functions unchanged
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=Settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Settings.SECRET_KEY, algorithm=Settings.ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, Settings.SECRET_KEY, algorithms=[Settings.ALGORITHM])
        return payload
    except JWTError:
        return None