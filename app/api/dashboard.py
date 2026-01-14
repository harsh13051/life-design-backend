from fastapi import APIRouter, HTTPException
from app.repository.activity_repo import ActivityRepository
from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

from app.repository.store import activity_repo as repo


@router.get("/{goal_id}")
def get_dashboard(goal_id: str):
    activities = repo.get_by_goal(goal_id)

    if not activities:
        raise HTTPException(status_code=404, detail="No activities found for this goal")

    return DashboardService.build_dashboard(goal_id, activities)
