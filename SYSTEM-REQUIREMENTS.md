# System Requirements Document (SRD) - THE IT CODE ACADEMY

**Project**: Web-based ICT & programming learning platform for youth in underserved communities  
**Builds directly on**: Assignment 3 SPECIFICATION.md (MVP scope, user roles, course/quiz/progress/certification/notification features)

## 1. Stakeholder Analysis
See separate file: [STAKEHOLDER-ANALYSIS.md](STAKEHOLDER-ANALYSIS.md) for the complete table (7 stakeholders with roles, concerns, pain points and metrics). All requirements below are traceable to these stakeholders.

## 2. Functional Requirements

1. The system shall allow users to register an account with email/password and select role (Student, Instructor or Admin).  
   *Acceptance criteria*: Email verification link sent; duplicate emails blocked.

2. The system shall authenticate users with secure login and enforce role-based access control (RBAC).

3. The system shall enable Instructors to create courses, upload lessons (text/video) and publish them.

4. The system shall allow Students to browse courses by title/topic and enroll in any free course.

5. The system shall permit Instructors to create multiple-choice quizzes with automatic grading and score storage.

6. The system shall track and display real-time student progress on a personal dashboard (lessons completed, quiz scores, course percentage).

7. The system shall process certification payments via integrated gateway (Stripe or PayFast) and update eligibility status on success.

8. The system shall send automated notifications (email via SendGrid, SMS via Twilio) for course updates, quiz reminders and payment confirmations.

9. The system shall allow Administrators to approve/delete user accounts and monitor platform usage.

10. The system shall generate and export weekly progress reports for Students and Parents/Guardians.

11. The system shall support lesson content upload (PDF/video) by Instructors with version control.

12. The system shall provide a search function that returns course results with real-time availability status.

(All functional requirements directly address pain points and concerns listed in the stakeholder table.)

## 3. Non-Functional Requirements

**Usability**  
- The user interface shall be fully responsive and comply with WCAG 2.1 accessibility standards (critical for low-bandwidth users in underserved communities).  
- The system shall provide tooltips and guided onboarding for first-time Students.

**Deployability**  
- The system shall be deployable on cloud platforms (Heroku or AWS Linux servers) using standard CI/CD pipelines.

**Maintainability**  
- All third-party integrations (Stripe, SendGrid, Twilio) shall include full API documentation and modular code structure.  
- The codebase shall use clear separation of concerns so new lesson types can be added without system-wide changes.

**Scalability**  
- The system shall support 1,000 concurrent users during peak hours (e.g., exam periods) with <5% performance degradation.

**Security**  
- All user data and payment information shall be encrypted using AES-256.  
- Authentication shall use HTTPS and JWT tokens with automatic session expiry.

**Performance**  
- Course pages and dashboards shall load in ≤3 seconds on average internet connections.  
- Quiz grading and notification dispatch shall complete in ≤1 second.

(All non-functional requirements are measurable and address the quality attributes listed in the assignment.)

## 4. Traceability Note
Every requirement above is explicitly linked to at least one stakeholder concern/pain point from the Stakeholder Analysis Table and the MVP scope in SPECIFICATION.md.
