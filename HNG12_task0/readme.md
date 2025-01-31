# Deploying a simple API using Fast API
This is project is a begineer guide to FastAPI ( Python Framefork )
Courtesy of HNG12

## Set Up your Environment
Set Up Python and FastAPI

- [x] install Python and ensure Python is running

```
python --version

```
- [x] On your project directory, create a virtual environment

```
python -m venv hngtask0

```

- [x] Activate VENV , (not pushed to github)

```
 hngtask0\Scripts\activate 

```

- [x] On your project directory, create your project file - main.py
> write your code

- [x] While VENV is active, install fastapi and requirement.txt

```
pip install fastapi uvicorn
pip freeze > requirements.txt


```

## How to Run the App Locally
- [x] Run the app

```
uvicorn main:app --host 0.0.0.0 --port 8000

```

- [x] View the API on http://localhost:8080

## Deployment to Render.com

## API Documentation
