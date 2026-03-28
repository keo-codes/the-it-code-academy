## USE CASE 1: Register Account

**Actor:** User
**Description:** Allows new users to create an account
**Preconditions:** User not registered
**Postconditions:** Account stored in database

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

**Actor:** User
**Description:** Authenticate user access
**Preconditions:** Account exists
**Postconditions:** User is logged in 

### Basic Flow
1. User enters email and password.
2. System verifies credentials and issues JWTT.
3. Access granted
4. System redirects to role-specific dashboard.

### Alternative Flow
- Invalid credentials -> Login failed (3 attempts lock account).
- Deny access

## USE CASE 3: Enroll Course

**Actor:** Student
**Description:** Student joins a course
**Preconditions:** Logged in
**Postconditions:** Enrollement recorded

### Basic Flow
1. Browse courses
2. Select course
3. Enroll
4. System confirms

### Alternative Flow
- Already enrolled -> message

## USE CASE 4: Access Lessons

**Actor:** Student
**Description:** View course content
**Preconditions:** Enrolled
**Postconditions:** Lesson marked accessed

### Basic Flow
1. Open course
2. Select lesson
3. Content displayed

## USE CASE 5: Take Quiz

**Actor:** Student
**Description:** Attempt quiz
**Preconditions:** Lesson completed
**Postconditions:** Score saved

### Basic Flow
1. Start quiz
2. Answer questions
3. Submit
4. Score calculated

### Alternative Flow
- Timeout -> auto-submit

## USE CASE 6: Creator Course

**Actor:** Instructor
**Description:** Create course content
**Preconditions:** Logged in
**Postconditions:** Course available

### Basic Flow
1. Enter details
2. Upload lessons
3. Save

## USE CASE 7: Purchase Certificate

**Actor:** Student
**Description:** Pay for certification 
**Preconditions:** Course completed
**Postconditions:** Payment record

### Basic Flow
1. Select certificate
2. Enter payment
3. Process payment
4. Confirmation sent

### Alternative Flow
- Payment fails -> retry

## USE CASE 8: View Progress 

**Actor:** Student/Instructor/Parent/Guardian
**Description:** View learning progress
**Preconditions:** Data exists
**Postconditions:** Progress displayed

### Basic Flow
1. Open dashboard
2. Retrieve data
3. Display result

