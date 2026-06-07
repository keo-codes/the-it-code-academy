import json
import os

class CourseService:
    """Service layer for Course business logic with persistence"""
    
    def __init__(self):
        self.file_path = "data/courses.json"
        self.courses = self._load_courses()

    def _load_courses(self):
        os.makedirs("data", exist_ok=True)
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _save_courses(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.courses, f, indent=2)

    def _get_course_by_id(self, course_id: int):
        return next((c for c in self.courses if c["course_id"] == course_id), None)

    def create_course(self, course_id: int, title: str, description: str, instructor_id: int = 1):
        if not title or not title.strip():
            raise ValueError("Course title is required")

        if self._get_course_by_id(course_id):
            raise ValueError(f"Course with ID {course_id} already exists.")

        course = {
            "course_id": course_id,
            "title": title,
            "description": description,
            "instructor_id": instructor_id
        }
        self.courses.append(course)
        self._save_courses()
        return course

    def get_all_courses(self):
        return self.courses

    def update_course(self, course_id: int, title: str = None, description: str = None):
        course = self._get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")

        if title is not None:
            if not title.strip():
                raise ValueError("Course title is required")
            course["title"] = title

        if description: course["description"] = description
        self._save_courses()
        return course

    def delete_course(self, course_id: int):
        course = self._get_course_by_id(course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} not found")

        self.courses.remove(course)
        self._save_courses()
        return f"Course {course_id} deleted successfully"