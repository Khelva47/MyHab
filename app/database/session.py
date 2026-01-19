from sqlmodel import SQLModel, create_engine, Session
from app.core.config import get_settings

settings = get_settings()

# MySQL engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,               # set True for SQL logs
    pool_pre_ping=True,       # avoids stale MySQL connections
    pool_recycle=1800         # MySQL idle timeout safety
)


def get_db():
    with Session(engine) as session:
        yield session
