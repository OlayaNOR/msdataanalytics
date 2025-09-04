from fastapi import APIRouter
from ..models import Package
from .. import crud
from ..utils.charts import generate_chart

router = APIRouter(
    prefix="/dataanalytics",
    tags=["DataAnalytics"],  
)

@router.get(
    "/stats",
    summary="Get package statistics",
    description="Returns a statistical summary of the packages grouped by state.",
    response_description="Dictionary with package statistics"
)
def stats():
    return "Packages stats."


@router.get(
    "/chart",
    summary="Get package chart",
    description="Returns a chart encoded in base64 representing the packages grouped by state.",
    response_description="Base64 encoded image"
)
def chart():
    return "Packages chart filtered by states."