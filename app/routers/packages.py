from fastapi import APIRouter
from ..models import Package
from .. import crud
from ..utils.charts import generate_chart

router = APIRouter(prefix="/packages", tags=["Packages"])

@router.post("/")
def add_package(package: Package):
    crud.insert_package(package.dict())
    return {"message": "Paquete insertado correctamente"}

@router.get("/stats")
def stats():
    data = crud.get_packages_grouped()
    return {"estadisticas": data}

@router.get("/chart")
def chart():
    data = crud.get_packages_grouped()
    img_base64 = generate_chart(data)
    return {"chart_base64": img_base64}