from fastapi import FastAPI
from db import Base, engine
from routes import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
