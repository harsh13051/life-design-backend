from typing import List
from app.models.activity import Activity
from app.services.journal_service import JournalService


class DashboardService:

    @staticmethod
    def build_dashboard(goal_id: str, activities: List[Activity]) -> dict:
        consistency_score = JournalService.calculate_consistency(activities)
        wellness_warning = JournalService.check_health_threshold(activities)

        return {
            "goal_id": goal_id,
            "total_activities": len(activities),
            "consistency_score": consistency_score,
            "wellness_warning": wellness_warning
        }
