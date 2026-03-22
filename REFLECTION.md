# Reflection – Challenges Faced in Balancing Stakeholder Needs

**Project**: THE IT CODE ACADEMY

The biggest challenge was balancing **free core access** (Students’ top priority) with **sustainable revenue** through paid certifications (needed by Administrators and Payment Providers). A purely free model would not cover third-party service costs (Stripe, Twilio), while forcing payment would exclude the underserved youth the platform targets. Solution: kept all lessons and quizzes free (addresses Students’ pain points) while making certification optional and clearly priced.

Another trade-off was **security vs usability**. Administrators and Payment Providers demanded AES-256 encryption, PCI-DSS compliance and strong authentication, but Students (many on low-end phones) need a simple, fast interface. We resolved this by implementing modern security under the hood (JWT + HTTPS) while keeping the UI clean and WCAG-compliant – no extra steps for students.

Scalability for community growth conflicted with deployment cost. IT Support Staff need reliable cloud scaling, but we cannot assume high budgets. We chose cloud-native deployability (Heroku/AWS) that starts free-tier and auto-scales, plus performance targets (≤3s load) that work on slow connections.

Notification reliability (SendGrid/Twilio) was tricky – high delivery rates boost retention for Students and Instructors, but dependency on external services introduces risk. We mitigated by requiring ≥95% delivery metric and fallback email paths.

Overall, the Agile approach allowed us to prioritise the MVP scope from Assignment 3 while keeping every requirement traceable and measurable. The biggest lesson: stakeholder needs are rarely perfectly aligned; success comes from explicit trade-offs documented with success metrics.
