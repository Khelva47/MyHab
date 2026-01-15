from pydantic import BaseModel, Field
from datetime import date, datetime

class StepCountCreate(BaseModel):
    user_id: str
    date: date
    steps: int = Field(default=0, ge=0)

class StepCountUpdate(BaseModel):
    steps: int = Field(..., ge=0)

class StepCountRead(BaseModel):
    id: str
    user_id: str
    date: date
    steps: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True