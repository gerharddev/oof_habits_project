# Habit Tracking Application

## 1. Overview

Everybody wants to stop unhealthy habits and create good habits in its place. They are turning to technology for assistance to achieving this. I was tasked to create a backend for a habit tracking application that will assist users to achieve their goals.

## 2. Running the project

### 2.1 Prerequisites

**Python 3.7** or later. (Python 3.10.3 was used for development)

### 2.2 Installing the project


## Using the project

### Running the cli

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

#### Start Rest API (Swagger UI)

```
python main.py start-rest-api
```

To see the OpenAPI documentation browse to
http://127.0.0.1:8000/docs

## Libraries used

- pylint
- pytest: For testing
- SQLAlcemy: Object relational mapper
- sqlite3: Database

## Testing

We are using pytest as our testing framework.
To run the test open your terminal in the habits_backend folder and run

```
pytest test_sample.py
```

## Rules

- dayly - 24 hours
- Montly
