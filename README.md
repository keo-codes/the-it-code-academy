# THE IT CODE ACADEMY

## Project Description

THE IT CODE ACADEMY is a web-based learning platform designed to provide **accessible ICT and programming education** to youth in underserved communities.

The platform allows learners to access **structured programming lessons**, complete **quizzes and assessments**, and **track their learning progress**. While learning content is free, users may optionally pay for **certification programs**.

The goal is to reduce barriers to digital education by providing an **affordable, structured, and accessible learning environment**.

---

## Getting Started

### Quick Local Setup

```bash
# Clone the repository
git clone https://github.com/keo-codes/the-it-code-academy.git
cd the-it-code-academy

# Backend setup
cd "Assignment 12"
pip install -r requirements.txt

# Run tests to verify everything works
python -m pytest tests/ -v
```

### Features Open for Contribution

| Feature                        | Status      | Difficulty | Ideal For              |
|--------------------------------|-------------|------------|------------------------|
| Redis Caching Layer            | Planned     | Medium     | Backend Developers     |
| Real-time Notifications        | Planned     | Medium     | Full-stack             |
| Mobile Responsive Improvements | In Progress | Easy       | Frontend               |
| Admin Analytics Dashboard      | Planned     | Hard       | Advanced               |
| Dark Mode Support              | Idea        | Easy       | UI/UX                  |
| Multi-language Support         | Idea        | Medium     | i18n Contributors      |

---

## Key Features

- Free ICT and programming lessons  
- Structured learning modules  
- Quiz and assessment system  
- Student progress tracking  
- Instructor course management  
- Optional paid certification  
- Notification support (email and SMS)  

---

## Documentation

### System Specification
Describes the **domain, problem, and system scope**.  
[SPECIFICATION.md](./SPECIFICATION.md)

### System Architecture
Contains **C4 diagrams** and system structure.  
[ARCHITECTURE.md](./ARCHITECTURE.md)

### Requirements & Analysis
- [Stakeholder Analysis Table](./STAKEHOLDER-ANALYSIS.md)  
- [System Requirements Document (SRD)](./SYSTEM-REQUIREMENTS.md)  

### Design & Testing
- [Use Case Specifications](./USE-CASE-SPECIFICATIONS.md)
- [Test Cases](./TEST-CASES.md)  

### Reflection
- [Final Reflection](Assignment%2015/REFLECTION.md)

---

## Repository Structure

```markdown
THE-IT-CODE-ACADEMY
│
├── README.md
├── SPECIFICATION.md
├── ARCHITECTURE.md
├── STAKEHOLDER-ANALYSIS.md
├── SYSTEM-REQUIREMENTS.md
├── USE-CASE-SPECIFICATIONS.md
├── TEST-CASES.md
├── Assignment 15/REFLECTION.md
│
└── C4-Diagrams
    ├── system-context-diagram.png
    ├── container-diagram.png
    └── component-diagram.png
```
---
## Assignment 8: Object State Modeling and Activity Workflow Modeling

- **[State Transition Diagrams + Editable draw.io files](Assignment%208/State-Transition-Diagrams.md)**  
- **[Activity Diagrams + Editable draw.io files](Assignment%208/Activity-Workflow-Diagrams.md)**  
- **[Traceability & Integration with Prior Work](Assignment%208/TRACEABILITY_INTEGRATION.md)**  
- **[Reflection](Assignment%208/REFLECTION.md)**

All diagrams are fully mapped to functional requirements (Assignment 4), use cases (Assignment 5), and Agile user stories (Assignment 6).

---

## Assignment 9: Domain Modeling and Class Diagram

**Deliverables** (located in the `Assignment 9` folder):

- **[Domain Model](Assignment%209/Domain%20Model.MD)**  
- **[Class Diagram in Mermaid](Assignment%209/Class%20Diagram%20in%20Mermaid.MD)**  
- **[Reflection](Assignment%209/Reflection.MD)**

**Overview**  
Completed a detailed domain model with 6 key entities, business rules, and a comprehensive UML class diagram using Mermaid.js. The design includes inheritance (Student/Instructor), composition (Course-Lesson), and an association class (Enrollment) to track progress — fully aligned with prior assignments.

**Key Highlights**  
- Maximum 5 active courses per student enforced  
- Clear separation of responsibilities  
- Dark-themed class diagram for better visibility  

All files are ready for review.

---

## Assignment 13: CI/CD Pipeline with GitHub Actions

### How to Run Tests Locally
```bash
cd "Assignment 12"
pip install -r requirements.txt
python -m pytest tests/ -v
```

## CI/CD Pipeline Overview

- **Branch Protection**: main branch is fully protected (requires PR + approval + passing tests).
- **CI Workflow** (.github/workflows/ci-cd.yml): Triggers on push and PR to main, runs full test suite.
- **CD Workflow**: Generates and uploads release ZIP artifact on merge to main.

All changes were made through Pull Requests. Pipeline is active and successful.

**Full details & screenshots**: [Assignment 13/Screenshots](Assignment%2013/Screenshots/)
