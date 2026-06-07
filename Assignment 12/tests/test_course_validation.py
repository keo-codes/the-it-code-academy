import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from services.course_service import CourseService


def test_create_course_rejects_duplicate_course_id(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    service = CourseService()

    first_course = service.create_course(101, "Python Basics", "Introductory Python course")

    with pytest.raises(ValueError, match="Course with ID 101 already exists"):
        service.create_course(101, "Python Basics Duplicate", "Duplicate course")

    assert service.get_all_courses() == [first_course]

    with open("data/courses.json") as courses_file:
        persisted_courses = json.load(courses_file)

    assert persisted_courses == [first_course]


def test_create_course_rejects_blank_title(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    service = CourseService()

    with pytest.raises(ValueError, match="Course title is required"):
        service.create_course(102, "   ", "Invalid title")

    assert service.get_all_courses() == []


def test_update_course_rejects_blank_title(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    service = CourseService()
    course = service.create_course(103, "Web Development", "Build web applications")

    with pytest.raises(ValueError, match="Course title is required"):
        service.update_course(103, title=" ")

    assert service.get_all_courses() == [course]
