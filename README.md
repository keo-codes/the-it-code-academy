# THE IT CODE ACADEMY

usecaseDiagram
    actor Student
    actor Instructor
    actor Administrator
    actor "Parent/Guardian" as Parent
    actor "Payment Gateway" as Payment
    actor "Notification Service" as Notification
    actor "IT Support Staff" as Support

    usecase "Register Account" as UC1
    usecase "Authenticate User" as UC2
    usecase "Browse Courses" as UC3
    usecase "Enroll in Course" as UC4
    usecase "Create Course" as UC5
    usecase "Upload Lesson Content" as UC6
    usecase "Create Quiz" as UC7
    usecase "Take Quiz" as UC8
    usecase "View Progress Dashboard" as UC9
    usecase "Process Certification Payment" as UC10
    usecase "Generate Progress Report" as UC11
    usecase "Manage User Accounts" as UC12
    usecase "Send Notification" as UC13

    Student --> UC1
    Student --> UC2
    Student --> UC3
    Student --> UC4
    Student --> UC8
    Student --> UC9
    Student --> UC10

    Instructor --> UC2
    Instructor --> UC5
    Instructor --> UC6
    Instructor --> UC7

    Administrator --> UC2
    Administrator --> UC11
    Administrator --> UC12

    Parent --> UC9
    Parent --> UC11

    Payment --> UC10
    Notification --> UC13

    UC4 ..> UC3 : <<include>>
    UC4 ..> UC2 : <<include>>
    UC8 ..> UC2 : <<include>>
    UC10 ..> UC13 : <<extend>>
    UC5 ..> UC2 : <<include>>
    UC6 ..> UC2 : <<include>>
    UC7 ..> UC2 : <<include>>
    UC9 ..> UC2 : <<include>>
    UC11 ..> UC2 : <<include>>
    UC12 ..> UC2 : <<include>>

## Project Description

THE IT CODE ACADEMY is a web-based learning platform designed to provide **accessible ICT and programming education** to youth in underserved communities.

The platform allows learners to access **structured programming lessons**, complete **quizzes and assessments**, and **track their learning progress** through an online system. While educational content is freely accessible, learners may optionally pay for **certification programs** to receive formal recognition of their skills.

The goal of the platform is to help reduce barriers to digital education by providing an **affordable, structured, and accessible learning environment**.

## Key Features

- Free ICT and programming lessons
- Structured learning modules
- Quiz and assessment system
- Student progress tracking
- Instructor course management
- Optional paid certification pathway
- Notification support (email and SMS)

---

## Documentation

### System Specification
This document describes the **system requirements, domain, problem statement, and scope** of THE IT CODE ACADEMY platform.

[SPECIFICATION.md](SPECIFICATION.md)

### System Architecture
This document contains the **C4 architectural diagrams** and explains the system structure, containers, and internal components.

[ARCHITECTURE.md](ARCHITECTURE.md)

---

## Repository Structure
---

```markdown
THE-IT-CODE-ACADEMY
│
├── README.md
├── SPECIFICATION.md
├── ARCHITECTURE.md
│
└── C4-Diagrams
    ├── system-context-diagram.png
    ├── container-diagram.png
    └── component-diagram.png
```
---
## Author

Student: Keorapetse Makhubo  
Course: Software Engineering  
Project: System Specification and Architectural Modeling

---

## Documentation
- [Stakeholder Analysis Table](STAKEHOLDER-ANALYSIS.md)
- [System Requirements Document (SRD)](SYSTEM-REQUIREMENTS.md)
- [Reflection on Stakeholder Needs](REFLECTION.md)
