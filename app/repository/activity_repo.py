from typing import List, Dict
from app.models.activity import Activity


class ActivityRepository:
    def __init__(self):
        # { goal_id: [Activity, Activity] }
        self._store: Dict[str, List[Activity]] = {}

    def add_activity(self, activity: Activity) -> None:
        if activity.goal_id not in self._store:
            self._store[activity.goal_id] = []
        self._store[activity.goal_id].append(activity)

    def get_by_goal(self, goal_id: str) -> List[Activity]:
        return self._store.get(goal_id, [])

    def get_all(self) -> Dict[str, List[Activity]]:
        return self._store
