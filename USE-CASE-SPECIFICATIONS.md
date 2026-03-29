# USE CASE SPECIFICATIONS 
## THE IT CODE ACADEMY SYSTEM

---

## Use Case 1: Create User Account  
**Actor:** Student / Instructor / Administrator  
**Supports:** FR-001  

**Description:** New users register for an account on the platform.  

**Preconditions:**  
- User is not registered  

**Postconditions:**  
- Account is created  
- Verification email is sent  

**Basic Flow:**  
1. User enters email, password, and selects role  
2. System validates email uniqueness  
3. System sends verification link  
4. User clicks verification link  
5. System activates account  

**Alternative Flows:**  
- Email already exists → Show error and prompt login  
- Verification link expires → Prompt resend  

---

## Use Case 2: Login  
**Actor:** Student / Instructor / Administrator / Parent/Guardian  
**Supports:** FR-002  

**Description:** User logs into the system (includes authentication).  

**Preconditions:**  
- Account exists  

**Postconditions:**  
- User is authenticated  
- User is redirected to dashboard  

**Basic Flow:**  
1. User enters email and password  
2. System authenticates user  
3. System generates JWT token  
4. Access is granted  

**Alternative Flows:**  
- Invalid credentials → Access denied  
- Account not verified → Prompt verification  

---

## Use Case 3: Browse Courses  
**Actor:** Student  
**Supports:** FR-005  

**Description:** Student searches and views courses.  

**Preconditions:**  
- User is logged in  

**Postconditions:**  
- Courses are displayed  

**Basic Flow:**  
1. Student enters search term or filters  
2. System returns matching courses  

**Alternative Flows:**  
- No results → Show message  

---

## Use Case 4: Enroll Course  
**Actor:** Student  
**Supports:** FR-006  

**Description:** Student enrolls in a course.  

**Preconditions:**  
- Student is logged in  
- Course is available  

**Postconditions:**  
- Enrollment is recorded  
- Progress tracking begins  

**Basic Flow:**  
1. Student selects course  
2. System checks availability  
3. Student confirms enrollment  
4. System records enrollment  

**Alternative Flows:**  
- Already enrolled → Show message  
- Course full → Offer waitlist  

---

## Use Case 5: Take Lessons  
**Actor:** Student  
**Supports:** FR-006  

**Description:** Student accesses lessons.  

**Preconditions:**  
- Student is enrolled  

**Postconditions:**  
- Lesson accessed  
- Progress updated  

**Basic Flow:**  
1. Student opens course  
2. Selects lesson  
3. Content is displayed  

**Alternative Flows:**  
- Lesson locked → Prompt prerequisite  

---

## Use Case 6: Take Quiz  
**Actor:** Student  
**Supports:** FR-008  

**Description:** Student completes a quiz.  

**Preconditions:**  
- Student is enrolled  
- Quiz is available  

**Postconditions:**  
- Score recorded  
- Progress updated  

**Basic Flow:**  
1. Student starts quiz  
2. Student answers questions  
3. Student submits quiz  
4. System grades automatically  
5. Results displayed  

**Alternative Flows:**  
- Time expires → Auto-submit  

---

## Use Case 7: Create Course  
**Actor:** Instructor  
**Supports:** FR-003  

**Description:** Instructor creates a course.  

**Preconditions:**  
- Instructor is logged in  

**Postconditions:**  
- Course saved  

**Basic Flow:**  
1. Instructor enters course details  
2. System saves course  

**Alternative Flows:**  
- Missing fields → Validation error  

---

## Use Case 8: Process Payment  
**Actor:** Student  
**Supports:** FR-010  

**Description:** Student processes payment for certification.  

**Preconditions:**  
- Course completed  

**Postconditions:**  
- Payment recorded  
- Status updated  

**Basic Flow:**  
1. Student selects certificate  
2. System processes payment  
3. Payment successful  
4. Status updated  

**Alternative Flows:**  
- Payment fails → Show error and retry option  
