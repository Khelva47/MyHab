import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic._internal._config")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.api.router import api_router
from app.core.logging import logger
from app.database.session import engine

app = FastAPI(
    title="Habit Tracker API",
    description="API for tracking daily habits, steps, and generating scorecards inspired by Atomic Habits",
    version="1.0.0"
)

# -----------------------------
# CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def on_startup():
    logger.info("Starting Habit Tracker API...")
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("Database connected and tables ensured")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise e

# -----------------------------
# Routers
# -----------------------------
app.include_router(api_router, prefix="/api/v1")

# -----------------------------
# Health & Root
# -----------------------------
@app.get("/")
def root():
    return {
        "message": "Welcome to Habit Tracker API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}

# -----------------------------
# Local dev entrypoint
# -----------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
