from app.models.activity import Activity
from typing import List, Dict


class InsightService:

    @staticmethod
    def generate_recommendation(all_activities: Dict[str, List[Activity]]) -> str:
        learning_total = 0
        health_total = 0

        for activities in all_activities.values():
            for activity in activities:
                if activity.activity_type == "Learning":
                    learning_total += activity.value
                elif activity.activity_type == "Health":
                    health_total += activity.value

        if learning_total >= 300 and health_total < 150:
            return "You are learning consistently, but consider rebalancing your growth plan by improving physical wellness."

        return "Your growth plan looks balanced. Keep up the good work!"
