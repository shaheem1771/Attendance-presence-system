from fastapi import FastAPI

app = FastAPI(
    title="Attendance Presence System API",
    version="1.0.0",
    description="Backend API for QR + GPS Attendance System"
)

@app.get("/")
def root():
    return {
        "message": "Attendance Presence System API is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
