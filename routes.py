from fastapi import APIRouter, HTTPException
from models import StudentCreate, StudentUpdate, StudentResponse
from database import db
from bson import ObjectId
from typing import List
from bson.errors import InvalidId

router = APIRouter()

def format_id(data):
    """Reformats MongoDB's _id to id."""
    if data:
        data['id'] = str(data.pop('_id'))
    return data

@router.post("/students", response_model=dict, status_code=201)
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    result = await db.students.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@router.get("/students", response_model=List[StudentResponse])
async def list_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await db.students.find(query).to_list(length=100)
    return [format_id(student) for student in students]

@router.get("/students/{id}", response_model=StudentResponse)
async def fetch_student(id: str):
    try:
        student = await db.students.find_one({"_id": ObjectId(id)})
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return format_id(student)

@router.patch("/students/{id}", status_code=204)
async def update_student(id: str, student: StudentUpdate):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    result = await db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if not result.matched_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return

@router.delete("/students/{id}", status_code=204)
async def delete_student(id: str):
    result = await db.students.delete_one({"_id": ObjectId(id)})
    if not result.deleted_count:
        raise HTTPException(status_code=404, detail="Student not found")
    return
