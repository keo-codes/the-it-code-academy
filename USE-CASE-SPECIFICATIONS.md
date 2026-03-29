# USE CASE SPECIFICATIONS
**THE IT CODE ACADEMY System**

## USE CASE 1: Create User Account

**Actor:** Student / Instructor / Administrator  
**Description:** New users register for an account on the IT Code Academy platform.  
**Preconditions:** User is not registered.  
**Postconditions:** Account is created and stored in the database; verification email is sent.  

**Basic Flow:** 
1. User enters email, password, and selects role.  
2. System validates email uniqueness and sends verification link.  
3. User clicks verification link.  
4. System activates the account.  

**Alternative Flows:**  
- Email already exists → Error message and suggestion to login instead.  
- Verification link expires → Prompt to resend verification.

## USE CASE 2: Login

**Actor:** Student / Instructor / Administrator / Parent  
**Description:** User logs into the system. **This use case includes the Authenticate use case.**  
**Preconditions:** Account exists.  
**Postconditions:** User is authenticated and redirected to role-specific dashboard.  

**Basic Flow:**  
1. User enters email and password.  
2. System **includes** the Authenticate use case.  
3. System verifies credentials and issues JWT token.  
4. Access is granted.  

**Alternative Flows:**  
- Invalid credentials → Login fails (after 3 attempts account is locked).  
- Account not verified → Prompt to verify email first.

## USE CASE 3: Browse Courses

**Actor:** Student  
**Description:** Student searches and views available courses.  
**Preconditions:** User is logged in.  
**Postconditions:** Course list is displayed with real-time availability.  

**Basic Flow:**  
1. Student enters search term or applies filters.  
2. System returns matching courses.  

**Alternative Flows:**  
- No results → “No courses found” message with suggestions.

## USE CASE 4: Enroll Course

**Actor:** Student  
**Description:** Student enrolls in a course. **This use case includes the Checks Availability use case.**  
**Preconditions:** Logged in and course is available.  
**Postconditions:** Enrollment recorded and progress tracking begins.  

**Basic Flow:**  
1. Student browses and selects course.  
2. System **includes** the Checks Availability use case.  
3. Student confirms enrollment.  
4. System records enrollment.  

**Alternative Flows:**  
- Already enrolled → “Already enrolled” message.  
- Course full → Waitlist option offered.

## USE CASE 5: Take Lessons

**Actor:** Student  
**Description:** Student accesses course lessons.  
**Preconditions:** Enrolled in the course.  
**Postconditions:** Lesson marked as accessed; progress updated.  

**Basic Flow:**  
1. Student opens enrolled course.  
2. Selects lesson.  
3. Content is displayed.  

**Alternative Flows:**  
- Lesson locked → Prompt to complete prerequisites.

## USE CASE 6: Take Quiz

**Actor:** Student  
**Description:** Student attempts a course quiz. **This use case includes the Checks Availability use case.**  
**Preconditions:** Enrolled in course and quiz is available.  
**Postconditions:** Score recorded and progress updated.  

**Basic Flow:**  
1. Student starts quiz.  
2. System **includes** the Checks Availability use case.  
3. Answers multiple-choice questions.  
4. Submits quiz.  
5. System auto-grades and shows results.  

**Alternative Flows:**  
- Time expires → Auto-submit with partial score.

## USE CASE 7: Create Course

**Actor:** Instructor  
**Description:** Instructor creates a new course.  
**Preconditions:** Instructor is logged in.  
**Postconditions:** Course is saved as draft and can be published.  

**Basic Flow:**  
1. Instructor enters title, description, topic.  
2. System saves draft.  

**Alternative Flows:**  
- Missing required fields → Validation error.

## USE CASE 8: Process Payment

**Actor:** Student  
**Description:** Student pays for certificate after course completion. **This use case includes the Payment Gateway use case and is extended by Handle Failed Payment.**  
**Preconditions:** Course completed.  
**Postconditions:** Payment recorded, certificate eligibility updated, notification sent.  

**Basic Flow:**  
1. Student selects certificate.  
2. System **includes** the Payment Gateway use case.  
3. Payment succeeds → Status updated.  

**Alternative Flows / Extension:**  
- Payment fails → The **Handle Failed Payment** use case is executed (<<extend>>).  
  - System shows error message and offers retry or alternative payment method.
