# System Architecture

## Project Title
THE IT CODE ACADEMY

## Domain
Education Technology (EdTech)

## Problem Statement
Youth in underserved communities need affordable access to ICT and programming education. THE IT CODE ACADEMY provides a **free and optionally paid online platform** with secure authentication, progress tracking, notifications, and certification options.

## Individual Scope
This architecture draft represents the MVP using **C4 modeling**. The system includes:

- **System Context Diagram**  
- **Container Diagram**  
- **Component Diagram**  
- **Dummy data support**  

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

**Diagram:**

```mermaid
flowchart TD
Student --> ElearningPlatform
Instructor --> ElearningPlatform
Administrator --> ElearningPlatform
ElearningPlatform --> PaymentGateway
ElearningPlatform --> EmailService
ElearningPlatform --> SMSService
ElearningPlatform --> Database
