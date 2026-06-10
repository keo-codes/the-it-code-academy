import json
import os

class EnrollmentService:
    """Service layer for Enrollment business logic with persistence"""
    
    def __init__(self, student_service):
        self.student_service = student_service
        self.file_path = "data/enrollments.json"
        # We use student_service.students for persistence

    def enroll_student(self, student_id: int, course_id: int):
        """Enroll student with business rule: max 5 courses"""
        student = self.student_service.get_student_by_id(student_id)
        
        if not student:
            raise ValueError(f"Student with ID {student_id} not found")
        
        # Business Rule
        if len(student.get("enrolled_courses", [])) >= 5:
            raise ValueError("Students cannot enroll in more than 5 courses")
        
        if course_id in student.get("enrolled_courses", []):
            raise ValueError("Student is already enrolled in this course")
        
        student["enrolled_courses"].append(course_id)
        
        # Save to persistent storage
        self.student_service._save_students()
        
        return {
            "message": f"Student {student_id} successfully enrolled in course {course_id}",
            "student": student
        }

    def get_student_courses(self, student_id: int):
        """Return the current course IDs for a student."""
        student = self.student_service.get_student_by_id(student_id)

        if not student:
            raise ValueError(f"Student with ID {student_id} not found")

        return {
            "student_id": student_id,
            "courses": student.get("enrolled_courses", []),
        }
