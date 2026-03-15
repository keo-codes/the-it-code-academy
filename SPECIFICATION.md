# System Specification

## Project Title
THE IT CODE ACADEMY

## Domain
Education Technology (EdTech)

## Domain Description
THE IT CODE ACADEMY is a web-based platform that provides **free basic ICT and programming lessons** to youth in underserved communities. The platform also offers a **paid membership** for learners who want certification. It is designed to be **secure, scalable, and user-friendly**, using **Java** for the backend and **Angular + VanillaJS** for the frontend.

## Problem Statement
Youth in underserved communities often lack access to affordable ICT education. Traditional educational institutions are expensive and require physical attendance. THE IT CODE ACADEMY addresses this gap by providing an online learning platform with:

- Free access to ICT and programming lessons  
- Optional paid certifications  
- Progress tracking  
- Notifications via email/SMS  
- Secure login and payment management  

## Individual Scope
This project focuses on **system specification and architectural modeling**. The MVP will include:

- **User Management:** registration, login, and role-based access (Student, Instructor, Admin)  
- **Course and Lesson Management:** CRUD for instructors, viewing for students  
- **Progress Tracking:** track lessons completed, quizzes taken  
- **Notifications:** email/SMS upon registration, course updates  
- **Subscriptions / Paid Memberships:** simulated payment and access control  
- **Security:** JWT authentication, HTTPS, hashed passwords  
- **Dummy Data Support:** pre-populated users, courses, lessons, and quizzes for testing  

### Features to Include in MVP
| Feature | Description |
|---------|------------|
| User Registration/Login | JWT-based authentication, role-based access |
| Courses & Lessons | CRUD operations for instructors, view-only for students |
| Quizzes | Multiple-choice quizzes with immediate feedback |
| Progress Tracking | Track lesson completion and quiz scores |
| Notifications | Email/SMS upon registration, course updates |
| Paid Memberships | Optional certification access, simulated payments |
| Security | HTTPS, hashed passwords, JWT, role-based access |
| Dummy Data | Pre-populated users, courses, lessons, quizzes |
