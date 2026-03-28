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

## USE CASE 3: Enroll Course

**Actor:** Student <br>
**Description:** Student joins a course <br>
**Preconditions:** Logged in <br>
**Postconditions:** Enrollement recorded <br>

### Basic Flow
1. Browse courses
2. Select course
3. Enroll
4. System confirms

### Alternative Flow
- Already enrolled -> message

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
**Description:** Attempt quiz <br>
**Preconditions:** Lesson completed <br>
**Postconditions:** Score saved <br>

### Basic Flow
1. Start quiz
2. Answer questions
3. Submit
4. Score calculated

### Alternative Flow
- Timeout -> auto-submit

## USE CASE 6: Creator Course

**Actor:** Instructor <br>
**Description:** Create course content <br>
**Preconditions:** Logged in <br>
**Postconditions:** Course available <br>

### Basic Flow
1. Enter details
2. Upload lessons
3. Save

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
**Preconditions:** Data exists <br>
**Postconditions:** Progress displayed <br>

### Basic Flow
1. Open dashboard
2. Retrieve data
3. Display result

