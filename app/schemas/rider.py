from pydantic import BaseModel

class RiderCreate(BaseModel):
    rider_id: str
    phone: str
    vehicle: str

class RiderResponse(BaseModel):
    id: int
    rider_id: str
    phone: str
    vehicle: str
    
    class Config:
        from_attributes = True

