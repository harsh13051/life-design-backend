from fastapi import FastAPI
from app.api import activities, dashboard, insights

app = FastAPI(title="Life Design Backend")

app.include_router(activities.router)
app.include_router(dashboard.router)
app.include_router(insights.router)

@app.get("/")
def root():
    return {"message": "Life Design Backend is running 🚀"}
