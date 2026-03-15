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

**Actors:**
- Student
- Instructor
- Administrator

**External Systems:**
- Payment Gateway (Stripe/PayFast)
- Email Service (SendGrid)
- SMS Service (Twilio)
  
````markdown
```` ```mermaid ````
C4Context
title System Context diagram for THE IT CODE ACADEMY

Person(student, "Student", "Youth in the community who enroll in courses and track progress.")
Person(instructor, "Instructor", "Creates and manages courses and quizzes.")
Person(admin, "Administrator", "Manages users, instructors, and system settings.")

System(elearning, "THE IT CODE ACADEMY System", "Allows students to access free lessons and paid certifications, track progress, and receive notifications.")

System_Ext(paymentGateway, "Payment Gateway (Stripe/PayFast)", "Processes payments for certification subscriptions.")
System_Ext(emailService, "Email Service (SendGrid)", "Sends notifications to students and instructors.")
System_Ext(smsService, "SMS Service (Twilio)", "Sends SMS notifications.")

Rel(student, elearning, "Uses to access lessons, take quizzes, track progress")
Rel(instructor, elearning, "Uses to create and manage courses and quizzes")
Rel(admin, elearning, "Uses to manage users and monitor platform")
Rel(elearning, paymentGateway, "Uses for subscription payments")
Rel(elearning, emailService, "Sends email notifications")
Rel(elearning, smsService, "Sends SMS notifications")
````

---

## Container Diagram

**Containers:**

- Web Application (Angular + VanillaJS)  
- Backend API (Java Spring Boot)  
- Notification Services (Email, SMS)
- Payment Service 

**Mermaid Diagram:**

````markdown
```` ```mermaid ````
C4Container
    title Container diagram for THE IT CODE ACADEMY

    Person(user, "User", "Student, Instructor, or Admin")

    Container(webApp, "Web Application", "Angular + VanillaJS", "Frontend for interacting with the platform")
    Container(api, "Backend API", "Java Spring Boot", "Handles business logic, authentication, and notifications")
    ContainerDb(database, "Database", "PostgreSQL/MySQL", "Stores users, courses, lessons, quizzes, progress, and payments")
    Container(payment, "Payment Service", "Stripe/PayFast", "Handles certification subscription payments")
    Container(notificationEmail, "Email Service", "SendGrid", "Sends email notifications")
    Container(notificationSMS, "SMS Service", "Twilio", "Sends SMS notifications")

    Rel(user, webApp, "Uses to access platform features")
    Rel(webApp, api, "Uses REST API to interact with backend")
    Rel(api, database, "Reads/Writes user, course, lesson, quiz, and progress data")
    Rel(api, payment, "Processes subscription payments")
    Rel(api, notificationEmail, "Sends email notifications")
    Rel(api, notificationSMS, "Sends SMS notifications")
````

---

## Component Diagram (Backend API)

**Components:**

- AuthService: registration, login, JWT authentication, role-based access  
- CourseService: manage courses and lessons  
- QuizService: manage quizzes and scoring
- ProgressService: track lesson completion and quiz scores
- PaymentService: handle subscriptions and certification access
- NotificationService: send emails/SMS notifications

**Mermaid Diagram:**

````markdown
```` ```mermaid ````
C4Component
    title Component diagram for Backend API

    Container(api, "Backend API", "Java Spring Boot") {
        Component(authService, "AuthService", "Handles user registration, login, JWT authentication, and role-based access")
        Component(courseService, "CourseService", "Manages courses and lessons CRUD")
        Component(quizService, "QuizService", "Manages quizzes, scoring, and answers")
        Component(progressService, "ProgressService", "Tracks lesson completion and quiz scores")
        Component(paymentService, "PaymentService", "Handles subscriptions and certification access")
        Component(notificationService, "NotificationService", "Sends email/SMS notifications")
        ComponentDb(database, "Database", "Stores users, courses, lessons, quizzes, progress, and payments")
    }

    Rel(authService, database, "Reads/Writes user data")
    Rel(courseService, database, "Reads/Writes course and lesson data")
    Rel(quizService, database, "Reads/Writes quiz and score data")
    Rel(progressService, database, "Reads/Writes progress data")
    Rel(paymentService, database, "Reads/Writes payment/subscription data")
    Rel(notificationService, database, "Reads/Writes notification logs")
````
