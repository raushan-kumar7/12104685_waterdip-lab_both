from fastapi import FastAPI
from api.database import engine
from api.database import Base
from api import models
from api.routes import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)