from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def read_root():
    return {
        "email": "chisomjude0205@gmail.com",
        "current_datetime":datetime.now(timezone.utc).isoformat(timespec='seconds') + "Z",
        "github_url": "https://github.com/ChisomJude/python-api/tree/master/HNG12_task0"
    }
