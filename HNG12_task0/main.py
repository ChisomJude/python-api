from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "email": "chisomjude0205@gmail.com",
        "current_datetime": datetime.now().isoformat(),
        "github_url": "https://github.com/ChisomJude/python-api/tree/master/HNG12_task0"
    }
