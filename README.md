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

<img width="950px;" src="https://res.cloudinary.com/cloud-alpha/image/upload/v1728845445/Common/task_dqgmmp.png"/>
<img width="950px;" src="https://res.cloudinary.com/cloud-alpha/image/upload/v1728842401/Common/task2_ig5pnq.png"/>

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

## Installation

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




# Hotel Booking Dashboard

The Hotel Booking Dashboard provides an overview of bookings with options to select a date range, view the number of adult and children visitors, and track daily visitor counts. It also displays visitors by country, offering valuable insights for managing occupancy and targeting international guests efficiently.

### Weblink: [Live Website](https://hotel-booking-dashboard-i4ea.onrender.com)

## Technologies Used

- **React.js** - JavaScript library for building user interfaces
- **React ApexCharts** - Data visualization library for React
- **ApexCharts** - JavaScript charting library for creating interactive charts
- **React Datepicker** - Date and time picker for React applications
- **Axios** - Promise-based HTTP client for making API requests
- **Tailwind CSS** - Utility-first CSS framework for styling

### Dashboard

<img width="1000px;" src="https://res.cloudinary.com/cloud-alpha/image/upload/v1728838872/Common/hotel_dashboard_tvpkqo.png"/>

### Installation

To run the frontend of the Hotel Booking Dashboard locally, follow these steps:

1. Clone the repository: `git clone https://github.com/raushan-kumar7/12104685_waterdip-lab_both.git`
2. Navigate to the frontend directory: `cd 12104685_frontend`
3. Install the dependencies: `npm install`
4. Start the server in development mode: `npm run dev`
5. Alternatively, to build the project for production: `npm run build`
6. The server will run at: `http://localhost:5173/`
