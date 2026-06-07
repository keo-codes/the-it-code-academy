from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="THE IT CODE ACADEMY - REST API",
    description="ASSIGNMENT 12: SERVICE LAYER + REST API IMPLEMENTATION",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import Services (now with persistence)
from services.student_service import StudentService
from services.course_service import CourseService
from services.enrollment_service import EnrollmentService

# Initialize Services
student_service = StudentService()
course_service = CourseService()
enrollment_service = EnrollmentService(student_service)

@app.get("/")
def root():
    return {"message": "✅ THE IT CODE ACADEMY API IS RUNNING - Assignment 12"}

# ===================== STUDENT CRUD =====================
# New endpoint to get a student's enrollments
@app.get("/api/students/{student_id}/enrollments")
def get_student_enrollments(student_id: int):
    try:
        return enrollment_service.get_student_courses(student_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/api/students")
def get_all_students():
    return student_service.get_all_students()

@app.post("/api/students")
def create_student(student_id: int, first_name: str, last_name: str, email: str):
    try:
        student = student_service.create_student(student_id, first_name, last_name, email)
        return {"message": "Student created successfully", "student": student}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/api/students/{student_id}")
def update_student(student_id: int, first_name: str = None, last_name: str = None, email: str = None):
    try:
        student = student_service.update_student(student_id, first_name, last_name, email)
        return {"message": "Student updated successfully", "student": student}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/students/{student_id}")
def delete_student(student_id: int):
    try:
        result = student_service.delete_student(student_id)
        return {"message": result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# ===================== COURSE CRUD =====================
@app.get("/api/courses")
def get_all_courses():
    return course_service.get_all_courses()

@app.post("/api/courses")
def create_course(course_id: int, title: str, description: str, instructor_id: int = 1):
    try:
        course = course_service.create_course(course_id, title, description, instructor_id)
        return {"message": "Course created successfully", "course": course}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/api/courses/{course_id}")
def update_course(course_id: int, title: str = None, description: str = None):
    try:
        course = course_service.update_course(course_id, title, description)
        return {"message": "Course updated successfully", "course": course}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.delete("/api/courses/{course_id}")
def delete_course(course_id: int):
    try:
        result = course_service.delete_course(course_id)
        return {"message": result}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

# ===================== ENROLLMENT (Business Logic) =====================
@app.post("/api/students/{student_id}/enroll")
def enroll_student(student_id: int, course_id: int):
    try:
        result = enrollment_service.enroll_student(student_id, course_id)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

print("THE IT CODE ACADEMY API IS READY!")
print("Visit: http://localhost:8000/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
