from pydantic import BaseModel
from datetime import datetime
from typing import Literal


class Activity(BaseModel):
    goal_id: str
    activity_type: Literal["Learning", "Health"]
    value: int  # minutes or reps
    timestamp: datetime
