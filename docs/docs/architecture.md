# Project Architecture

## Frontend

- React
- TypeScript
- Tailwind CSS
- React Router
- Axios

---

## Backend

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication

---

## Authentication Flow

Student Login
↓

JWT Token
↓

Authorized API Requests

Teacher Login
↓

JWT Token
↓

Admin Dashboard

---

## Attendance Flow

Teacher Starts Session
↓

QR Code Generated
↓

Student Scans QR

↓

GPS Verification

↓

Attendance Recorded

↓

Dashboard Updated
