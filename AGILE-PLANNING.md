# AGILE USER STORIES, BACKLOG, & SPRINT PLANNING

**Project:** The IT Code Academy  
**Repository:** [https://github.com/keo-codes/the-it-code-academy](https://github.com/keo-codes/the-it-code-academy)  
**GitHub Project Board:** [IT Code Academy Backlog](https://github.com/keo-codes/the-it-code-academy/projects) (click **Product Backlog** and **Sprint 1** views)  
**Author:** Keo-codes  
**Date:** April 2026

---

## Objective
Apply Agile methodology by translating system requirements (Assignment 4) and use cases (Assignment 5) into user stories, creating a prioritized product backlog, and planning the first sprint for a Minimum Viable Product (MVP).

**Traceability Note:**  
All user stories are directly mapped to functional requirements (FR-XXX) from `SYSTEM-REQUIREMENTS.md` and use cases from `USE-CASE-SPECIFICATIONS.md` / `USE-CASE-DIAGRAM.md`.

---

## 1. User Story Creation (30 Marks)

**12 user stories** created (8+ from functional requirements + 4+ from use cases).  
All stories follow the required format and meet **INVEST** criteria.

**View all user stories as GitHub Issues:** [Issues → label:user-story](https://github.com/keo-codes/the-it-code-academy/issues?q=is%3Aissue+label%3Auser-story)

### User Stories Table

| Story ID | User Story | Acceptance Criteria | Priority (High/Medium/Low) | Traceability |
|----------|------------|---------------------|----------------------------|--------------|
| US-001 | As a new user (Student/Instructor/Admin), I want to create an account with email, password and role selection so that I can access the platform after verification. | Email verification sent; duplicate emails blocked; account activated on link click. | High | FR-001 + UC: Create User Account |
| US-002 | As a user, I want to log in securely with email/password so that I can access my role-based dashboard. | Valid credentials grant access + JWT; invalid credentials show error; unverified accounts prompted to verify. | High | FR-002 + UC: Login |
| US-003 | As a student, I want to browse courses by title or topic so that I can find relevant learning materials quickly. | Search/filter results load ≤3s; courses displayed with availability status; “No results” message shown. | High | FR-005 + UC: Browse Courses |
| US-004 | As a student, I want to enroll in a course so that I can start learning and have progress tracking enabled. | Enrollment recorded only if course available; confirmation displayed; already-enrolled message shown. | High | FR-006 + UC: Enrol Course |
| US-005 | As an instructor, I want to upload lesson content (text/video/PDF) with version control so that students always have up-to-date materials. | Content saved with version history; accessible to enrolled students only. | High | FR-004 |
| US-006 | As an instructor, I want to create and publish courses so that students can discover and enroll in structured learning paths. | Course saved and immediately visible to students after publish. | High | FR-003 + UC: Create Course |
| US-007 | As an instructor, I want to create multiple-choice quizzes linked to courses so that I can assess student understanding. | Quiz saved and attached to specific course/lesson. | Medium | FR-007 |
| US-008 | As a student, I want to take a quiz with automatic grading so that I receive instant feedback on my performance. | Quiz submitted → score calculated and stored; results displayed immediately; auto-submit on time expiry. | High | FR-008 + UC: Take Quiz |
| US-009 | As a student, I want to view my real-time progress dashboard so that I can track completion of lessons, quizzes and courses. | Dashboard updates instantly after any activity. | High | FR-009 |
| US-010 | As a student, I want to process payment for certification so that I can receive an official credential after completing a course. | Payment gateway processes successfully/fails gracefully; status updated. | Medium | FR-010 + UC: Process Payment |
| US-011 | As any user, I want to receive automated email/SMS notifications so that I stay informed about deadlines, progress and updates. | Notifications delivered within defined time limits. | Medium | FR-011 |
| US-012 | As an administrator, I want to manage user accounts so that I can maintain platform security and support users. | Admin can view/edit/block users; changes applied immediately. | Low | FR-012 |

**Non-Functional Story (example as per assignment):**  
As a system administrator, I want all user data encrypted with AES-256 and HTTPS enforced so that security compliance is met.

---

## 2. Product Backlog Creation (30 Marks)

**MoSCoW prioritization** applied. Effort estimates use **Fibonacci story points**.

**View full Product Backlog (GitHub Project):** [Product Backlog View](https://github.com/keo-codes/the-it-code-academy/projects) → select **Product Backlog**

### Product Backlog Table

| Story ID | User Story (short)              | Priority (MoSCoW) | Effort (story points) | Dependencies     |
|----------|---------------------------------|-------------------|-----------------------|------------------|
| US-001   | Create account                  | Must-have         | 3                     | None             |
| US-002   | Login                           | Must-have         | 3                     | US-001           |
| US-003   | Browse courses                  | Must-have         | 5                     | None             |
| US-004   | Enroll in course                | Must-have         | 3                     | US-002, US-003   |
| US-008   | Take quiz                       | Must-have         | 5                     | US-004           |
| US-009   | View real-time progress         | Must-have         | 3                     | US-004, US-008   |
| US-005   | Upload lesson content           | Should-have       | 5                     | US-006           |
| US-006   | Create & publish course         | Should-have       | 5                     | None             |
| US-007   | Create quiz (instructor)        | Should-have       | 3                     | US-006           |
| US-011   | Receive notifications           | Should-have       | 2                     | None             |
| US-010   | Process payment for cert        | Could-have        | 5                     | US-008           |
| US-012   | Manage users (admin)            | Could-have        | 3                     | US-001           |

**Justification of Prioritization:**  
Must-have stories deliver the complete student learning flow (register → login → find → enroll → learn → assess → track progress). These directly support the MVP value from the project specification: free, accessible ICT education for underserved youth. Should-have items enable instructors to create content (core to the platform’s mission). Could-have items (payment, admin) are important but not required for the first working version. This keeps the backlog focused and prevents scope creep.

---

## 3. Sprint Planning (30 Marks)

**Sprint 1 Goal (2-week sprint):**  
“Deliver a functional MVP core that allows new students to register, log in, browse available courses, enroll, complete a quiz, and view their real-time progress — enabling the first end-to-end learning experience.”

**Selected for Sprint 1 (6 stories – total 22 story points):**  
US-001, US-002, US-003, US-004, US-008, US-009

**View Sprint 1 Kanban Board:** [Sprint 1 View](https://github.com/keo-codes/the-it-code-academy/projects) → select **Sprint 1**

### Sprint Backlog Table

| Task ID | Task Description                                      | Assigned To | Estimated Hours | Status    |
|---------|-------------------------------------------------------|-------------|-----------------|-----------|
| T-001   | Implement user registration API + email verification  | Dev Team    | 8               | To Do     |
| T-002   | Build login page + JWT authentication                 | Dev Team    | 6               | To Do     |
| T-003   | Create course browsing UI + search/filter backend     | Dev Team    | 10              | To Do     |
| T-004   | Develop enrollment logic + database recording         | Dev Team    | 5               | To Do     |
| T-005   | Build quiz taking interface + automatic grading engine| Dev Team    | 12              | To Do     |
| T-006   | Create real-time progress dashboard (frontend + API)  | Dev Team    | 7               | To Do     |
| T-007   | Write unit/integration tests for auth & enrollment    | Dev Team    | 4               | To Do     |
| T-008   | Deploy Sprint 1 to staging environment                | Dev Team    | 3               | To Do     |

**Sprint Goal Contribution to MVP:**  
By the end of this sprint, students will be able to complete the full “discover → join → learn & assess” cycle. This validates the core value proposition of The IT Code Academy and provides a working product ready for stakeholder demo.

---

## 4. GitHub Agile Tools Used (as required)

- **GitHub Issues** – 12 user stories created as issues with acceptance criteria, priorities, and tasks  
- **GitHub Project** – “IT Code Academy Backlog” with two Kanban Board views:  
  - [Product Backlog view](https://github.com/keo-codes/the-it-code-academy/projects) (all 12 stories)  
  - [Sprint 1 view](https://github.com/keo-codes/the-it-code-academy/projects) (filtered to 6 sprint stories)  
- **Labels** – `user-story`, `enhancement`, `must-have`, `should-have`, `could-have`, `sprint-1`  
- **Milestone** – “Sprint 1” linked to the selected stories

---

## 5. Reflection (Challenges in Prioritization, Estimation, and Aligning Agile with Stakeholder Needs)

Working as the sole stakeholder, product owner, Scrum Master, and developer created an interesting internal tension that mirrored real-world Agile resistance. My first instinct was to push every feature into the Must-have column — instructor course creation, payments, notifications, admin tools, reports — because I know how valuable they all are to the mission of free ICT education. This scope-creep urge felt like the classic stakeholder pressure I would face in a real project.  

The Agile principle of “maximizing value while minimizing waste” forced me to repeatedly ask: “What is the smallest thing that delivers learning value right now?” This internal negotiation was difficult; I literally argued with myself about whether enrollment could wait until after payments. In the end, strict MoSCoW and the MVP definition won — only the student learning flow became Must-have.  

Estimation was equally challenging without a team. I had no historical velocity, so I used Fibonacci points conservatively and added buffer tasks (testing, deployment). I overestimated some UI work (e.g., quiz interface) because I know from previous assignments how complex responsive design + real-time updates can become. The 22-point sprint feels achievable in two weeks but still stretches me — exactly the kind of healthy tension Agile encourages.  

Traceability to Assignments 4 and 5 was straightforward because the repo already contained clean FR and UC documents, but mapping every story back to them revealed small gaps (e.g., version control on lessons was only implied). This exercise improved the overall specification.  

The biggest personal learning was how Agile forces ruthless focus. As the only stakeholder I could have approved every “nice-to-have,” yet the methodology made me protect the MVP. This mirrors the real difficulty teams face when stakeholders want everything yesterday. By experiencing that resistance internally, I now better understand why product owners must be decisive and why the backlog must remain dynamic.  

Overall, this assignment transformed the static requirements from Assignments 4–5 into living, prioritized work that is ready for actual development. The GitHub Issues + Project board will serve as the single source of truth going forward.
