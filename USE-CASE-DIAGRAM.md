# IT Code Academy - Use Case Diagram (Mermaid.js)

```mermaid
usecase
    left to right direction

    actor "Student" as Student
    actor "Instructor" as Instructor
    actor "Administrator" as Admin
    actor "Parent/Guardian" as Parent
    actor "Payment Gateway" as PaymentGateway
    actor "Notification Service" as NotificationService

    rectangle "IT Code Academy System" {
        usecase "Create User Account" as UC1
        usecase "Login" as UC2
        usecase "Authenticate" as UC3
        usecase "Browse Courses" as UC4
        usecase "Enroll Course" as UC5
        usecase "Take Lessons" as UC6
        usecase "Take Quiz" as UC7
        usecase "View Student Progress" as UC8
        usecase "Create Course" as UC9
        usecase "Upload Lessons" as UC10
        usecase "Create Quiz" as UC11
        usecase "Process Payment" as UC12
        usecase "Send Notifications" as UC13
        usecase "Manage Users" as UC14
        usecase "Generate Student Report" as UC15
        usecase "Checks Availability" as UC16
        usecase "Handle Failed Payment" as UC17
    }

    Student --> UC1
    Student --> UC2
    Student --> UC4
    Student --> UC5
    Student --> UC6
    Student --> UC7
    Student --> UC8
    Student --> UC12

    Instructor --> UC9
    Instructor --> UC10
    Instructor --> UC11
    Instructor --> UC8

    Admin --> UC14
    Admin --> UC15
    Admin --> UC1

    Parent --> UC8
    Parent --> UC13

    PaymentGateway ..> UC12 : <<include>>
    NotificationService ..> UC13 : <<include>>

    UC2 ..> UC3 : <<include>>
    UC5 ..> UC16 : <<include>>
    UC7 ..> UC16 : <<include>>
    UC17 -.-> UC12 : <<extend>>
