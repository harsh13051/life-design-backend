from datetime import date
from typing import List
from app.models.activity import Activity


class JournalService:

    @staticmethod
    def calculate_consistency(activities: List[Activity]) -> float:
        if not activities:
            return 0.0

        dates = sorted({activity.timestamp.date() for activity in activities})

        consecutive_days = 1
        max_streak = 1

        for i in range(1, len(dates)):
            if (dates[i] - dates[i - 1]).days == 1:
                consecutive_days += 1
                max_streak = max(max_streak, consecutive_days)
            else:
                consecutive_days = 1

        return round(max_streak / len(dates), 2)

    @staticmethod
    def check_health_threshold(activities: List[Activity]) -> bool:
        health_minutes = sum(
            activity.value for activity in activities
            if activity.activity_type == "Health"
        )
        return health_minutes < 150
