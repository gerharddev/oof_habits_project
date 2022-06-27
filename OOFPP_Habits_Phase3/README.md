# Habit Tracking Application

## 1. Overview

Everybody wants to stop unhealthy habits and create good habits in its place. They are turning to technology for assistance to achieving this. I was tasked to create a backend for a habit tracking application that will assist users to achieve their goals.

## 2. Running the project

### 2.1 Prerequisites

**Python 3.7** or later. (Python 3.10.3 was used for development). Download the latest version [here](https://www.python.org/downloads/)

### 2.2 Installing the project

- Open CommandPrompt on Windows or Terminal on Mac after cloning the project from github
- Go to the root folder of your project where you will see a setup.py file
- Run the following command

  ```
  pip install .
  ```

- If you see `Successfully installed OOFPP-Habits-Phase3-1.0` the project is ready to be run.

## 3. Using the project

### 3.1 Running the cli

```
python main.py --help
```

```
python main.py analyse-tracked-habits
```

```
python analyse-equal-periodicity --frequency daily
```

```
python main.py analyse-streak-habit --habit_id 1
```

```
python main.py analyse-longest-streak
```

python main.py start-rest-api
python main.py habit-cli --add Test
python main.py habit-cli --command Test

### 3.2 Start Rest API (Swagger UI)

```
python main.py start-rest-api
```

To see the OpenAPI documentation browse to
http://127.0.0.1:8000/docs

### 3.3 Running the tests

We are using pytest as our testing framework.
To run the test open your terminal in the tests folder and run

```
pytest habits_backend/test_main.py
```

## 4. Libraries used

- pylint
- pytest: For testing
- SQLAlcemy: Object relational mapper
- sqlite3: Database

## Testing

## Rules

- dayly - 24 hours
- Montly
