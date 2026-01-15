from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class CompletionCreate(BaseModel):
    habit_id: str
    date: date
    completed_count: int = Field(default=1, ge=0)
    notes: Optional[str] = ""

class CompletionUpdate(BaseModel):
    completed_count: int = Field(..., ge=0)
    notes: Optional[str] = None

class CompletionRead(BaseModel):
    id: str
    habit_id: str
    date: date
    completed_count: int
    notes: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True