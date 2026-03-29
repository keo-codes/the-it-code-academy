# SYSTEM SPECIFICATION

## Project Title
THE IT CODE ACADEMY

---

## 1. Introduction

### 1.1 Domain

The system operates within the **Education Technology (EdTech)** domain. Education Technology focuses on using digital platforms to improve access to education, learning resources, and skills development.

THE IT CODE ACADEMY provides an online platform where students learn programming and ICT skills through structured lessons, quizzes, and certification programs.

The platform supports youth in underserved communities by providing accessible and affordable digital education. Students access content, track progress, and obtain certifications, while instructors manage courses and assessments.

---

### 1.2 Problem Statement

Many young people in underserved communities face barriers to accessing quality ICT and programming education. Traditional institutions are often expensive, inaccessible, or lack modern resources.

Existing online platforms may require subscriptions or lack localized support.

THE IT CODE ACADEMY addresses these challenges by providing:

- Free access to programming lessons  
- Structured beginner-friendly courses  
- Quizzes for assessment  
- Student progress tracking  
- Optional paid certification  
- Notification services for engagement  

The system provides an accessible and structured digital learning environment for skill development.

---

### 1.3 Individual Scope (MVP)

This project implements a **Minimum Viable Product (MVP)** of the THE IT CODE ACADEMY platform.

---

#### User Management

The system supports three user roles:

- **Student** – Enroll Course, Take Lessons, Take Quiz, View Student Progress  
- **Instructor** – Create Course, Upload Lessons, Create Quiz  
- **Administrator** – Manage Users and system operations  

---

#### Course Management

**Instructors can:**
- Create Course  
- Upload Lessons  
- Manage course content  

**Students can:**
- Browse Courses  
- Enroll Course  
- Access lessons  

---

#### Quiz and Assessment System

- Create Quiz  
- Multiple-choice questions  
- Automatic grading  
- Score storage  

---

#### Progress Tracking

The system tracks:

- Lessons completed  
- Quiz results  
- Course completion progress  

Students view progress via dashboard.

---

#### Certification and Payments

- Process Payment via third-party gateway (Stripe or PayFast)  
- Certification eligibility tracking  

---

#### Notifications

The system sends notifications via:

- Email (SendGrid)  
- SMS (Twilio)  

Used for:
- Course updates  
- Quiz reminders  
- Payment confirmations  
- System announcements  

---

## 2. System Features

### 2.1 Create User Account & Authenticate User
- Create User Account  
- Login  
- Authenticate User  
- Role-based access control  

---

### 2.2 Course Management
- Create Course  
- Upload Lessons  
- Modify course content  
- Browse Courses  
- Enroll Course  
- Access lessons  

---

### 2.3 Quiz Management
- Create Quiz  
- Attempt quizzes  
- Automatic grading  
- Score recording  

---

### 2.4 Progress Tracking
- Track completed lessons  
- Track quiz scores  
- Display course progress  

---

### 2.5 Certification and Payments
- Process Payment  
- Certification tracking  

---

### 2.6 Notification System
- Send Notifications (email/SMS)  
- Course announcements  
- Quiz reminders  
- Payment confirmations  

---

## 3. System Users

### Student
- Create User Account and Login  
- Browse Courses  
- Enroll Course  
- Take Lessons  
- Take Quiz  
- View Student Progress  
- Process Payment for certification  

---

### Instructor
- Create Course  
- Upload Lessons  
- Create Quiz  
- Monitor student progress  

---

### Administrator
- Manage Users  
- Monitor system activity  
- Maintain system operations  

---

## 4. System Constraints

- Internet connection required  
- Payment depends on third-party gateway  
- Notifications depend on external services  

---

## 5. Assumptions

- Dummy data used for initial testing  
- Access via web browser  
- External services may be simulated during development  

---

## 6. Future Improvements

- Mobile application support  
- Video-based lessons  
- AI-based recommendations  
- Discussion forums  
- Gamification (badges, leaderboards)  
