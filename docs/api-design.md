# Attendance Presence System - API Design

## Authentication

POST /api/auth/student/login
POST /api/auth/student/register

POST /api/auth/teacher/login
POST /api/auth/teacher/register

---

## Students

GET /api/students
GET /api/students/{id}
PUT /api/students/{id}
DELETE /api/students/{id}

---

## Teachers

GET /api/teachers
GET /api/teachers/{id}

---

## Classes

POST /api/classes
GET /api/classes
GET /api/classes/{id}
PUT /api/classes/{id}
DELETE /api/classes/{id}

---

## Attendance Sessions

POST /api/sessions/start
POST /api/sessions/end
GET /api/sessions

---

## QR Code

GET /api/qr/{session_id}

---

## Attendance

POST /api/attendance/check-in
GET /api/attendance/history
GET /api/attendance/class/{class_id}
