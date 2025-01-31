Set Up Python and FastAPI

[ x ] install Python and ensure Python is running

```
python --version

```
[ x ] On your project directory, create a virtual environment

```
python -m venv hngtask0

```

[x] Activate Venv

```
 hngtask0\Scripts\activate 

```

[x] On your project directory, create your project file - main.py
> write your code

[x] While VENV is active, install fastapi 

```
pip install fastapi uvicorn

```

[x] Run the app

```
uvicorn main:app --host 0.0.0.0 --port 8000

```

[x] View the API on http://localhost:8080
