## USE CASE 1: Register Account

**Actor:** User <br>
**Description:** Allows new users to create an account <br>
**Preconditions:** User not registered <br>
**Postconditions:** Account stored in database <br>

### Basic Flow
1. User enters email, password, and selects role
2. System validates email is unique and sends verification link
3. User clicks verification link
4. System activates account
5. Account creation verification sent

### Alternative Flow
- Email already exists -> error message and suggestion to login
- Verification link expires -> prompt to resend

## USE CASE 2: Login

**Actor:** User <br>
**Description:** Authenticate user access <br>
**Preconditions:** Account exists <br>
**Postconditions:** User is logged in <br>

### Basic Flow
1. User enters email and password.
2. System verifies credentials and issues JWTT.
3. Access granted
4. System redirects to role-specific dashboard.

### Alternative Flow
- Invalid credentials -> Login failed (3 attempts lock account).
- Deny access

## USE CASE 3: Authenticate User

**Actor:** User <br>
**Description:** Secure login with RBAC <br>
**Preconditions:** User is logged in <br>

### Basic Flow
1. User enters email and password.
2. System verifies credentials and issues JWTT.
3. Access granted
4. System redirects to role-specific dashboard.

### Alternative Flow
- Invalid credentials -> Login failed (3 attempts lock account).
- Deny access

## USE CASE 4: Login

**Actor:** User <br>
**Description:** Authenticate user access <br>
**Preconditions:** Account exists <br>
**Postconditions:** User is logged in <br>

### Basic Flow
1. User enters email and password.
2. System verifies credentials and issues JWTT.
3. Access granted
4. System redirects to role-specific dashboard.

### Alternative Flow
- Invalid credentials -> Login failed (3 attempts lock account).
- Deny access

## USE CASE 5: Browse Courses

**Actor:** Student <br>
**Description:** Search and view available courses <br>
**Preconditions:** User is logged in <br>
**Postconditions:** Course list displayed with real-time status <br>

### Basic Flow
1. Student enters search term or filters by topic
2. System returns matching courses

### Alternative Flow
- No results -> "No courses found" suggestion

## USE CASE 6: Enroll in Course

**Actor:** Student <br>
**Description:** Student enrolls in a free course <br>
**Preconditions:** Logged in, course id free and available <br>
**Postconditions:** Enrollement recorded, progress tracking starts <br>

### Basic Flow
1. Browse courses
2. Select course
3. Enroll
4. System confirms enrollment

### Alternative Flow
- Course already enrolled -> message "Already enrolled".

## USE CASE 4: Access Lessons

**Actor:** Student <br>
**Description:** View course content <br>
**Preconditions:** Enrolled <br>
**Postconditions:** Lesson marked accessed <br>

### Basic Flow
1. Open course
2. Select lesson
3. Content displayed

## USE CASE 5: Take Quiz

**Actor:** Student <br>
**Description:** Attempt a multi-choice quiz <br>
**Preconditions:** Enrolled in course with quiz available <br>
**Postconditions:** Score recorded and progress updated <br>

### Basic Flow
1. Start quiz
2. Answer questions
3. Submit
4. System presents questions with auto-grading on submission

### Alternative Flow
- Timeout -> auto-submit

## USE CASE 6: Creator Course

**Actor:** Instructor <br>
**Description:** Create course content <br>
**Preconditions:** Logged in <br>
**Postconditions:** Course available and can be published <br>

### Basic Flow
1. Enter details such as Title, description, topic
2. System saves draft

### Already Flows
- Missing required fields -> validation error

## USE CASE 7: Purchase Certificate

**Actor:** Student <br>
**Description:** Pay for certification <br>
**Preconditions:** Course completed <br>
**Postconditions:** Payment record <br>

### Basic Flow
1. Select certificate
2. Enter payment
3. Process payment
4. Confirmation sent

### Alternative Flow
- Payment fails -> retry

## USE CASE 8: View Progress 

**Actor:** Student/Instructor/Parent/Guardian <br>
**Description:** View learning progress <br>
**Preconditions:** Logged in <br>
**Postconditions:** Dashboard displays completion %, quiz scores <br>

### Basic Flow
1. User open dashboard
2. System retrieves and displays data

### Alternative Flows
- No data yet -> "Start your first course" prompt

## USE CASE 9: Process Certificate Payment

**Actor:** Student <br>
**Description:** Handles paid certification via external gateway <br>
**Preconditions:** Student completed required courses <br>
**Postconditions:** Payment recorded, certification eigibility updated, notification sent <br>

### Basic Flow
1. Student initiates payment
2. System redirects to gateway
3. On success, updates status and triggers notification

### Alternative Flow
- Payment fails -> error message and retry option

