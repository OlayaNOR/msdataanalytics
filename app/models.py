from pydantic import BaseModel

class Package(BaseModel):
    tracking_id: str
    estado: str