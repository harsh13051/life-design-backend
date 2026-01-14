# 🧠 Life Design Backend – Growth Journal Service

## 📌 Project Overview
The **Life Design Backend** is a Python-based microservice built using **FastAPI**.  
It serves as the backend for a *Life Design Dashboard*, allowing users to log growth-related activities, analyze consistency, monitor wellness thresholds, and receive productivity recommendations.

The project is designed with **modular architecture**, **clean separation of concerns**, and **scalability in mind**, following real-world backend engineering practices.

---

## 🚀 Tech Stack
- Python 3.x  
- FastAPI  
- Uvicorn  
- Pydantic  
- In-memory Repository Pattern  

---

## 📂 Project Structure

life-design-backend/
├── app/
│ ├── api/
│ │ ├── activities.py
│ │ ├── dashboard.py
│ │ └── insights.py
│ ├── models/
│ │ └── activity.py
│ ├── services/
│ │ ├── journal_service.py
│ │ ├── dashboard_service.py
│ │ └── insight_service.py
│ ├── repository/
│ │ ├── activity_repo.py
│ │ └── store.py
│ └── main.py
├── requirements.txt
└── README.md

### 
1️⃣ Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Start the Server
uvicorn app.main:app --reload

📄 API Documentation (Swagger)

Once the server is running, open:

http://127.0.0.1:8000/docs

🔗 API Endpoints
✅ POST /activities

Log a user activity toward a goal.

Request Body

{
  "goal_id": "goal_1",
  "activity_type": "Learning",
  "value": 60,
  "timestamp": "2026-01-14T10:00:00"
}

✅ GET /dashboard/{goal_id}

Returns a summary of activities for a specific goal.

Response

{
  "goal_id": "goal_1",
  "total_activities": 3,
  "consistency_score": 0.67,
  "wellness_warning": true
}

✅ GET /insights/optimization

Returns a productivity recommendation based on stored activity data.

Response

{
  "recommendation": "You are learning consistently, but consider rebalancing your growth plan by improving physical wellness."
}



The system follows a service-oriented architecture, where all business logic related to data interpretation—such as consistency scoring, health threshold checks, and recommendations—is encapsulated within a dedicated service layer. This keeps API routes lightweight and focused solely on request handling and response formatting.

To maintain efficiency as activity data grows, aggregation logic is implemented using optimized patterns such as single-pass summations and set-based date calculations. The repository pattern abstracts data access, enabling seamless replacement of the in-memory store with a persistent database (e.g., PostgreSQL or MongoDB) without changing the core business logic.
