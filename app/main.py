from fastapi import FastAPI
from .routers import packages  

app = FastAPI(
    title="Packages Tracker API",
    description="API for data analytics on packages",
    version="1.0.0"
)

app.include_router(packages.router)