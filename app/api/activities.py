from fastapi import APIRouter
from app.models.activity import Activity
from app.repository.activity_repo import ActivityRepository

router = APIRouter(prefix="/activities", tags=["Activities"])

from app.repository.store import activity_repo as repo



@router.post("/")
def log_activity(activity: Activity):
    repo.add_activity(activity)
    return {
        "message": "Activity logged successfully",
        "activity": activity
    }
