# Use Case Diagram - IT Code Academy

**Assignment 5: Use Case Modeling**

This diagram shows all actors and use cases for the IT Code Academy system, fully aligned with the functional requirements from Assignment 4 and the original `.drawio` file.

## Use Case Diagram (Mermaid)

```mermaid
graph LR
    %% =============================================
    %% ACTORS (shown as circles)
    %% =============================================
    Student((Student))
    Instructor((Instructor))
    Admin((Administrator))
    Parent((Parent/Guardian))
    PaymentGateway((Payment Gateway))
    NotificationService((Notification Service))

    %% =============================================
    %% SYSTEM BOUNDARY
    %% =============================================
    subgraph "IT Code Academy System"
        direction TB

        UC1([Create User Account])
        UC2([Login])
        UC3([Authenticate])
        UC4([Browse Courses])
        UC5([Enroll Course])
        UC6([Take Lessons])
        UC7([Take Quiz])
        UC8([View Student Progress])
        UC9([Create Course])
        UC10([Upload Lessons])
        UC11([Create Quiz])
        UC12([Process Payment])
        UC13([Send Notifications])
        UC14([Manage Users])
        UC15([Generate Student Report])
        UC16([Checks Availability])
        UC17([Handle Failed Payment])
    end

    %% =============================================
    %% RELATIONSHIPS
    %% =============================================
    %% Student interactions
    Student --> UC1
    Student --> UC2
    Student --> UC4
    Student --> UC5
    Student --> UC6
    Student --> UC7
    Student --> UC8
    Student --> UC12

    %% Instructor interactions
    Instructor --> UC9
    Instructor --> UC10
    Instructor --> UC11
    Instructor --> UC8

    %% Administrator interactions
    Admin --> UC14
    Admin --> UC15
    Admin --> UC1

    %% Parent interactions
    Parent --> UC8
    Parent --> UC13

    %% External services
    PaymentGateway -.->|<<include>>| UC12
    NotificationService -.->|<<include>>| UC13

    %% Internal includes & extends
    UC2 -.->|<<include>>| UC3
    UC5 -.->|<<include>>| UC16
    UC7 -.->|<<include>>| UC16
    UC17 -.->|<<extend>>| UC12

    %% Styling - makes use cases look like UML ovals
    classDef usecase fill:#f9f,stroke:#333,stroke-width:2px;
    class UC1,UC2,UC3,UC4,UC5,UC6,UC7,UC8,UC9,UC10,UC11,UC12,UC13,UC14,UC15,UC16,UC17 usecase
