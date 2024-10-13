# Task Management - FastAPI

This FastAPI-based Task Management API allows users to create, read, update, and delete tasks. Key features include listing tasks, managing tasks individually by ID, bulk task creation, and bulk deletion. It supports multiple endpoints for task operations with a simple and efficient interface.

### Weblink: [Live Website](https://task-fastapi.onrender.com/docs)

## Features

- **FastAPI**: A high-performance framework for building APIs.
- **SQLAlchemy**: An ORM for database interaction.
- **Pydantic**: Data validation and settings management.
- **PostgreSQL**: The database used in this project.
- **Uvicorn**: ASGI server for running the FastAPI app.
- **Dotenv**: Manage environment variables using a `.env` file.

## Prerequisites

Make sure you have the following installed:

- Python 3.7+
- PostgreSQL

## Project Structure

```bash
.
├── api/
│   ├── __init__.py        # Initialize the api package
│   ├── main.py            # The main FastAPI app
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas for data validation
│   ├── database.py        # Database connection and session setup
│   └── routes.py          # API routes
│
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables file (should not be committed to git)
├── .env.sample            # Sample environment variables file for reference
├── .gitignore             # Git ignore file to specify untracked files
├── Pipfile                # Pipenv file for managing dependencies
├── Pipfile.lock           # Pipenv lock file
└── README.md              # Project documentation (this file)
```

### Task API Image

<img width="900px;" src="https://res.cloudinary.com/cloud-alpha/image/upload/v1728842388/Common/task1_erbiqq.png"/>
<img width="900px;" src="https://res.cloudinary.com/cloud-alpha/image/upload/v1728842401/Common/task2_ig5pnq.png"/>

## API Endpoints

### Task Routes

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| GET    | `/v1/tasks`           | List all tasks               |
| POST   | `/v1/tasks`           | Create a new task            |
| GET    | `/v1/tasks/{task_id}` | Get a specific task by ID    |
| PUT    | `/v1/tasks/{task_id}` | Update a specific task by ID |
| DELETE | `/v1/tasks/{task_id}` | Delete a specific task by ID |
| DELETE | `/v1/tasks/bulk`      | Bulk delete tasks            |
| POST   | `/v1/tasks/bulk`      | Bulk create multiple tasks   |

### Installation

To run the backend of the Task Management FastAPI locally, follow these steps:

1. Clone the repository: `git clone https://github.com/raushan-kumar7/12104685_waterdip-lab_both.git`
2. Navigate to the backend directory:: `cd 12104685_backend`
3. Set up a virtual environment: Using `Pipenv`: `pipenv install` and `pipenv shell` Or using `venv` and `pip`:

   ```bash
     python3 -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
     pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory for environment variables (based on `.env.sample`) : `DATABASE_URL=your_postgres_database_url`
5. Run the FastAPI app: `uvicorn api.main:app --reload`
6. The server will run at: `http://127.0.0.1:8000`
7. You can access the FastAPI documentation at: `http://127.0.0.1:8000/docs`
