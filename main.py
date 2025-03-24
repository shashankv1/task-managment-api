from fastapi import FastAPI
from database import engine, Base
from routers import auth, tasks

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth.router)
app.include_router(tasks.router)
