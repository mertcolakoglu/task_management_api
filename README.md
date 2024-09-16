# Project Management API

This Django REST Framework project provides a comprehensive API for project management, including user authentication, project creation, task management, and notifications.

## Table of Contents
- [Project Management API](#project-management-api)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Project](#running-the-project)
  - [API Endpoints](#api-endpoints)
    - [Authentication](#authentication)
    - [User Profile](#user-profile)
    - [Projects](#projects)
    - [Tasks](#tasks)
    - [Notifications](#notifications)
  - [Authentication](#authentication-1)
  - [Models](#models)
    - [User](#user)
    - [Profile](#profile)
    - [Project](#project)
    - [TeamMember](#teammember)
    - [Task](#task)
    - [Comment](#comment)
    - [Notification](#notification)
  - [Permissions](#permissions)
  - [Signals](#signals)

## Features

- User registration and authentication using JWT tokens
- Profile management
- Project creation and management
- Task creation, assignment, and status tracking
- Commenting on tasks
- Notification system for task assignments, updates, and comments
- Role-based permissions for project members

## Requirements

- Python 3.8+
- Django 5.0+
- Django REST Framework 3.14+
- djoser 2.2+
- djangorestframework-simplejwt 5.3+

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mertcolakoglu/task_management_api.git
   cd task_management_api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory and add the following:
   ```
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   ```

2. Make sure to replace `your_secret_key_here` with a secure secret key.

3. Configure your database settings in `core/settings.py` if you want to use a different database (the project currently uses SQLite).

## Running the Project

1. Apply the database migrations:
   ```
   python manage.py migrate
   ```

2. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- `/auth/jwt/create/` (POST) - Obtain JWT token
- `/auth/jwt/refresh/` (POST) - Refresh JWT token
- `/auth/users/` (POST) - Register a new user
- `/auth/users/me/` (GET, PUT, PATCH) - Retrieve or update the authenticated user

### User Profile
- `/api/me/` (GET, PUT, PATCH) - Retrieve or update user profile

### Projects
- `/api/projects/` (GET, POST) - List all projects or create a new project
- `/api/projects/<int:pk>/` (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific project
- `/api/projects/<int:project_id>/members/` (GET, POST) - List all team members or add a new team member to a project
- `/api/projects/<int:project_id>/members/<int:member_id>/` (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific team member

### Tasks
- `/api/tasks/` (GET, POST) - List all tasks or create a new task
- `/api/tasks/<int:pk>/` (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific task
- `/api/tasks/<int:task_id>/comments/` (GET, POST) - List all comments or add a new comment to a task
- `/api/tasks/<int:task_id>/comments/<int:pk>/` (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific comment

### Notifications
- `/api/notifications/` (GET, POST) - List all notifications or create a new notification
- `/api/notifications/<int:pk>/` (GET, PUT, PATCH, DELETE) - Retrieve, update, or delete a specific notification
- `/api/notifications/mark-all-read/` (POST) - Mark all notifications as read

## Authentication

This project uses JWT (JSON Web Tokens) for authentication. To authenticate, follow these steps:

1. Obtain a token by sending a POST request to `/auth/jwt/create/` with your username and password.
2. Include the token in the Authorization header of your requests:
   ```
   Authorization: JWT <your_token_here>
   ```

## Models

### User
Custom user model with email as the username field.

### Profile
Extended user profile with additional information.

### Project
Represents a project with team members.

### TeamMember
Represents a user's role in a project (Owner, Manager, or Member).

### Task
Represents a task within a project, with assignee, status, and priority.

### Comment
Represents comments on tasks.

### Notification
Represents notifications for various actions (task assignment, updates, comments).

## Permissions

Custom permissions are implemented to control access to various parts of the API:

- `IsProjectOwnerOrManager`: Allows access only to project owners or managers.
- `IsTeamMemberOrReadOnly`: Allows read access to all team members, but write access only to the assigned user or task creator.
- `IsAssignedOrCreatorOrReadOnly`: Allows read access to all, but write access only to the assigned user or task creator.
- `IsOwner`: Allows access only to the owner of the object.

## Signals

The project uses Django signals to automatically create notifications when:

- A task is created or updated
- A comment is added to a task

These notifications are sent to the relevant users (e.g., task assignee).