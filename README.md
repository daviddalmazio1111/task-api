# Task Management API

A REST API for managing tasks.

## Tech Stack

- **FastAPI**: Python web framework used to build the API
- **PostgreSQL**: Database that stores all the tasks
- **Docker**: Containerizes FastAPI and PostgreSQL and links them together

## Prerequisites

- **Docker** (required): to run the application
- **pgAdmin** (optional): to visualize the data stored in the database

## How to Run

Clone this repository and open a terminal in the project folder. Run the following command:

    docker compose up

Then open your browser and go to http://localhost/docs to access the API interface.

## Data Model

A task is composed of three fields:

| Field | Type | Description |
|-------|------|-------------|
| id | int | Unique identifier of the task |
| task | string | Description of the task |
| owner | string | Person responsible for the task |

## Project Structure

- **models.py**: Defines the structure of the PostgreSQL table that stores the tasks. The table has three columns: id (int) which is the primary key, task (string) which contains the description of the task, and owner (string) which represents the person responsible for the task.

- **database.py**: Establishes the connection with the PostgreSQL database using SQLAlchemy. It creates the database engine, initializes the tables and provides a session to interact with the database.

- **main.py**: Sets up the FastAPI application and defines all the API routes: GET to retrieve all tasks, POST to create a new task and DELETE to remove a task by its id. It uses the session from database.py to interact with the database.

- **Dockerfile**: Defines the environment of the container where the application runs. It uses Python 3.9, installs all the required dependencies from requirements.txt and exposes the application on port 80 via uvicorn.

- **docker-compose.yml**: The orchestrator of the project. It creates two containers — one for the FastAPI application and one for PostgreSQL — puts them in the same internal network so they can communicate, and exposes the ports to make them accessible from your machine.

## API Routes

| Method | URL | Description |
|--------|-----|-------------|
| GET | /tasks | Returns all tasks in the database |
| POST | /tasks | Takes an id, a task and an owner and adds it to the database |
| DELETE | /tasks/{id} | Deletes a task from the database by its id |

## Usage

Once the application is running, you can interact with the API via http://localhost/docs 

### Get all tasks
```
GET /tasks
```

### Create a task
```
POST /tasks
```
Body:
```json
{
    "id": 1,
    "task": "Buy groceries",
    "owner": "John"
}
```

### Delete a task
```
DELETE /tasks/1
```


