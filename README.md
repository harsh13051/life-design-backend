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

The system follows a service-oriented architecture, where all business logic related to data interpretation—such as consistency scoring, health threshold checks, and recommendations—is encapsulated within a dedicated service layer. This keeps API routes lightweight and focused solely on request handling and response formatting.

To maintain efficiency as activity data grows, aggregation logic is implemented using optimized patterns such as single-pass summations and set-based date calculations. The repository pattern abstracts data access, enabling seamless replacement of the in-memory store with a persistent database (e.g., PostgreSQL or MongoDB) without changing the core business logic.