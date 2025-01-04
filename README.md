# TaskForge - Task Management API

TaskForge is a robust REST API built with Django REST Framework that provides task management functionality with user authentication. Users can create, manage and track tasks while maintaining proper access control.

## Features

- User authentication using JWT (JSON Web Tokens)
- Create and manage tasks with status tracking
- Role-based access control (Admin/Regular users)
- API documentation with Swagger/ReDoc
- Filter tasks by status
- Secure password handling

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Oyshik-ICT/TaskForge.git
cd TaskForge/
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Documentation

You can explore and test the API using Swagger UI or ReDoc:
- Swagger UI: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- ReDoc: `http://127.0.0.1:8000/api/schema/redoc/`

## API Endpoints

### Authentication
- `POST /api/token/` - Obtain JWT token pair
  - Provide username and password to get access token
- `POST /api/token/refresh/` - Refresh JWT token
  - Provide refresh token to get new access token

### User Management
- `GET /user/` - List all users (Admin only)
- `POST /user/` - Create new user (Public access)
- `GET /user/{id}/` - Retrieve user details (Own account only)
- `PUT/PATCH /user/{id}/` - Update user details (Own account only)
- `DELETE /user/{id}/` - Delete user account (Own account only)

### Task Management
- `GET /tasks/` - List tasks
  - Admin can see all tasks
  - Regular users can only see their own tasks
  - Filter tasks by status using query parameter: `/tasks/?status=Pending`
- `POST /tasks/` - Create new task (Authenticated users)
- `GET /tasks/{id}/` - Retrieve task details
- `PUT/PATCH /tasks/{id}/` - Update task
- `DELETE /tasks/{id}/` - Delete task

## Task Status Options
- Pending
- In Progress
- Complete

## Using Swagger UI for Testing

1. Open Swagger UI at `http://127.0.0.1:8000/api/schema/swagger-ui/`
2. Click "Authorize" and enter your JWT token:
   - First get a token from `/api/token/`
   - In the authorize popup, type: `Bearer <your_token>`
3. You can now test all endpoints directly from Swagger UI

## API Authentication

All requests (except user creation) require authentication. Include the JWT token in the Authorization header:
```
Authorization: Bearer <your_token>
```


## Security Features

- Password hashing using Django's security features
- JWT authentication with refresh tokens
- User-specific data isolation
- Role-based access control

