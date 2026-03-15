# System Architecture

## Project Title
THE IT CODE ACADEMY

## Domain
Education Technology (EdTech)

## Problem Statement
Youth in underserved communities often lack affordable access to ICT and programming education. THE IT CODE ACADEMY provides an online learning platform with free lessons, optional paid certification, progress tracking, and notifications.

## Individual Scope
This document models the **MVP architecture** using the **C4 model**. The system includes:

- System Context Diagram
- Container Diagram
- Component Diagram
- Support for dummy data to simulate users, courses, lessons, quizzes, and payments.

---

## System Context Diagram

![System Context Diagram](C4-Diagrams/System%20Context%20Diagram.png)

Actors:
- Student
- Instructor
- Administrator

External Systems:
- Payment Gateway (Stripe/PayFast)
- Email Service (SendGrid)
- SMS Service (Twilio)

---

## Container Diagram

![Container Diagram](C4-Diagrams/Container%20Diagram.png)

Containers:

- Web Application (Angular + VanillaJS)
- Backend API (Java Spring Boot)
- Notification Services (Email, SMS)
- Payment Service

---

## Component Diagram (Backend API)

![Component Diagram](C4-Diagrams/Component%20Diagram.png)

Components:

- AuthService: registration, login, JWT authentication, role-based access  
- CourseService: manage courses and lessons  
- QuizService: manage quizzes and scoring  
- ProgressService: track lesson completion and quiz scores  
- PaymentService: handle subscriptions and certification access  
- NotificationService: send emails/SMS notifications
