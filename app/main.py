from fastapi import FastAPI
from .routers import packages

app = FastAPI(title="Microservicio de Análisis de Paquetes")

app.include_router(packages.router)

@app.get("/")
def root():
    return {"message": "Bienvenido al microservicio de análisis"}