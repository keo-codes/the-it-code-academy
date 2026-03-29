# THE IT CODE ACADEMY TEST CASES

## Functional Test Cases 

| Test Case ID | Requirement ID | Description                          | Steps                                                                 | Expected Result                                   | Actual Result | Status (Pass/Fail) |
|--------------|----------------|--------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------|---------------|--------------------|
| TC-001       | FR-001         | Create user account                  | 1. Go to register 2. Enter email/password/role 3. Verify email       | Account created + verification email sent        | -             | -                  |
| TC-002       | FR-002         | User logs in successfully            | 1. Enter valid email/password 2. Click Login                         | Redirected to dashboard                          | -             | -                  |
| TC-003       | FR-005         | Student browses courses              | 1. Login 2. Search "Python"                                          | Matching courses displayed                       | -             | -                  |
| TC-004       | FR-006         | Student enrolls in course            | 1. Browse 2. Select course 3. Click Enroll                           | Enrollment confirmed                             | -             | -                  |
| TC-005       | FR-006         | Student takes a lesson               | 1. Open enrolled course 2. Select lesson                             | Lesson displayed + progress updated              | -             | -                  |
| TC-006       | FR-008         | Student completes quiz               | 1. Start quiz 2. Answer questions 3. Submit                          | Score recorded + progress updated                | -             | -                  |
| TC-007       | FR-003         | Instructor creates course            | 1. Login as instructor 2. Enter details 3. Save                      | Course saved                                     | -             | -                  |
| TC-008       | FR-010         | Student processes payment            | 1. Complete course 2. Select certificate 3. Pay                      | Payment successful + status updated              | -             | -                  |

---

## Non-Functional Test Scenarios

### NF-001: Performance Test  
Simulate 500 concurrent students browsing courses and enrolling.  
**Expected Result:** Response time ≤ 2 seconds for 95% of requests.

### NF-002: Security Test  
Attempt login with invalid credentials 5 times.  
**Expected Result:**  
- Account is locked for 30 minutes  
- No JWT token is issued  
- All endpoints require valid authentication
