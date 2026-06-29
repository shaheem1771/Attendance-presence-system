# Attendance Presence System - Database Design

## Students

- id
- full_name
- roll_number
- email
- password_hash
- department
- semester
- created_at

---

## Teachers

- id
- full_name
- email
- password_hash
- department
- created_at

---

## Classes

- id
- course_code
- course_name
- teacher_id
- latitude
- longitude
- radius
- created_at

---

## Attendance Sessions

- id
- class_id
- qr_token
- start_time
- end_time
- status

---

## Attendance Records

- id
- student_id
- session_id
- check_in_time
- latitude
- longitude
- status
