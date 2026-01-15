from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class HabitCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: Optional[str] = ""
    g0al: int = Field(default=1, ge=1, le=100)

class HabitUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    description: Optional[str] = None
    goal: Optional[int] = Field(None, ge=1, le=100)

class HabitRead(BaseModel):
    id: str
    user_id: str
    name: str
    description: Optional[str]
    goal: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True