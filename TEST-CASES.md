# THE IT CODE ACADEMY TEST CASES

```markdown

## Functional Test Cases 

| Test Case ID | Requirement ID | Description                          | Steps                                                                 | Expected Result                          | Actual Result | Status (Pass/Fail) |
|--------------|----------------|--------------------------------------|-----------------------------------------------------------------------|------------------------------------------|---------------|--------------------|
| TC-001       | FR-001         | Student creates new account          | 1. Go to register 2. Enter email/password/role 3. Verify email      | Account created + verification email sent| -             | -                  |
| TC-002       | FR-002         | User logs in successfully            | 1. Enter valid email/password 2. Click Login                         | Redirected to dashboard                  | -             | -                  |
| TC-003       | FR-003         | Student browses courses              | 1. Login 2. Search "Python"                                          | List of matching courses displayed       | -             | -                  |
| TC-004       | FR-004         | Student enrolls in course            | 1. Browse 2. Select course 3. Click Enroll                          | Enrollment confirmed                     | -             | -                  |
| TC-005       | FR-005         | Student takes a lesson               | 1. Enrolled course 2. Open lesson                                   | Lesson content displayed + progress updated | -          | -                  |
| TC-006       | FR-006         | Student completes quiz               | 1. Start quiz 2. Answer questions 3. Submit                          | Score recorded + progress updated        | -             | -                  |
| TC-007       | FR-007         | Instructor creates course            | 1. Login as instructor 2. Fill course details 3. Save               | Course saved as draft                    | -             | -                  |
| TC-008       | FR-008         | Student processes certificate payment| 1. Complete course 2. Select certificate 3. Pay                     | Payment successful + notification sent   | -             | -                  |

## Non-Functional Test Scenarios

**Performance Test (NF-001):**  
Simulate 500 concurrent students browsing courses and enrolling. Verify response time ≤ 2 seconds for 95% of requests.

**Security Test (NF-002):**  
Attempt login with invalid credentials 5 times → Account must be locked for 30 minutes. Verify JWT token is not issued on failed login and all API endpoints require valid authentication.
