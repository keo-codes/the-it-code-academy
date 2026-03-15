# System Architecture

## Project Title
THE IT CODE ACADEMY

## Domain
Education Technology (EdTech)

## Problem Statement
Youth in underserved communities often lack affordable access to ICT and programming training. THE IT CODE ACADEMY provides a scalable online platform to deliver free learning modules and optional paid certifications.

## Individual Scope
This project models the architecture of THE IT CODE ACADEMY using the **C4 model**:

- System Context Diagram
- Container Diagram
- Component Diagram

---

# C4 System Context Diagram

```mermaid
flowchart TD

Student --> ElearningPlatform
Instructor --> ElearningPlatform
Administrator --> ElearningPlatform

ElearningPlatform --> PaymentGateway
ElearningPlatform --> Database
