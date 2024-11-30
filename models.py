from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class StudentCreate(BaseModel):
    name: str
    age: int
    address: Address

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    address: Address
