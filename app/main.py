import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .database import get_db, check_db_connection
from . import models
from .database import engine, Base

# Create all tables on startup
Base.metadata.create_all(bind=engine)

MY_REG_NO = os.getenv("STUDENT_REG_NO", "YOURREGNUM")  # ← PUT YOUR REG NUMBER HERE

app = FastAPI(title="DevOps Student Registry")


class StudentCreate(BaseModel):
    name: str
    reg_no: str
    course: str


class StudentOut(BaseModel):
    id: int
    name: str
    reg_no: str
    course: str

    class Config:
        from_attributes = True


@app.get("/health")
def health_check():
    db_ok = check_db_connection()
    return {
        "status": "ok",
        "db": "connected" if db_ok else "disconnected",
        "student": MY_REG_NO
    }


@app.post("/students", response_model=StudentOut, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()


@app.get("/students/{reg_no}", response_model=StudentOut)
def get_student(reg_no: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(
        models.Student.reg_no == reg_no
    ).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student