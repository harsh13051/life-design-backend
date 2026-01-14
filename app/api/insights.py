from fastapi import APIRouter
from app.repository.store import activity_repo
from app.services.insight_service import InsightService

router = APIRouter(prefix="/insights", tags=["Insights"])


@router.get("/optimization")
def get_optimization_insight():
    all_activities = activity_repo.get_all()
    recommendation = InsightService.generate_recommendation(all_activities)

    return {
        "recommendation": recommendation
    }
