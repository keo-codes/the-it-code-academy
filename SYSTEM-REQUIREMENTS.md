# SYSTEM REQUIREMENTS DOCUMENT (SRD)
## THE IT CODE ACADEMY

**Project:** Web-based ICT & programming learning platform for youth in underserved communities  
**Builds on:** [SPECIFICATION.md](./SPECIFICATION.md)

---

## 1. Stakeholder Analysis
See: [STAKEHOLDER-ANALYSIS.md](./STAKEHOLDER-ANALYSIS.md)

All requirements below are derived from stakeholder roles, concerns, pain points, and success metrics.

---

## 2. Functional Requirements

| ID | Requirement | Acceptance Criteria |
|----|------------|-------------------|
| **FR-001** | The system shall allow users to create an account with email, password, and role selection (Student, Instructor, Administrator). | Email verification is sent and duplicate emails are blocked. |
| **FR-002** | The system shall authenticate users and enforce role-based access control (RBAC). | Only valid credentials grant access with correct permissions. |
| **FR-003** | The system shall allow instructors to create and publish courses. | Course is saved and visible to students. |
| **FR-004** | The system shall allow instructors to upload lesson content (text, video, PDF) with version control. | Content is accessible and version history is maintained. |
| **FR-005** | The system shall allow students to browse courses by title or topic. | Results display relevant courses with availability status. |
| **FR-006** | The system shall allow students to enroll in courses. | Enrollment confirmation is displayed. |
| **FR-007** | The system shall allow instructors to create multiple-choice quizzes. | Quiz is saved and linked to course content. |
| **FR-008** | The system shall allow students to complete quizzes with automatic grading. | Score is calculated and stored. |
| **FR-009** | The system shall display real-time student progress. | Dashboard updates immediately after activity. |
| **FR-010** | The system shall process certification payments via a payment gateway. | Payment status updates on success or failure. |
| **FR-011** | The system shall send automated notifications (email/SMS). | Notifications are delivered within defined time limits. |
| **FR-012** | The system shall allow administrators to manage users. | Admin actions are applied successfully. |
| **FR-013** | The system shall generate weekly progress reports. | Reports are downloadable and accurate. |

---

## 3. Non-Functional Requirements

### Usability
- The system shall provide a responsive interface.
- The system shall comply with WCAG 2.1 accessibility standards.
- The system shall provide onboarding guidance for new users.

### Deployability
- The system shall be deployable on cloud platforms (e.g., AWS, Linux servers).
- The system shall support CI/CD pipelines.

### Maintainability
- The system shall use modular architecture.
- The system shall include API documentation for integrations.

### Scalability
- The system shall support at least 1,000 concurrent users.

### Security
- The system shall encrypt data using AES-256.
- The system shall use HTTPS and JWT authentication.

### Performance
- The system shall load pages within 3 seconds.
- The system shall process quizzes and notifications within 1 second.

---

## 4. Alignment Statement

All requirements align with:
- Stakeholder concerns defined in [STAKEHOLDER-ANALYSIS.md](./STAKEHOLDER-ANALYSIS.md)
- System scope defined in [SPECIFICATION.md](./SPECIFICATION.md)
