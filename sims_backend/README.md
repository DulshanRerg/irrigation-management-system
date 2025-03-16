# SIMS Backend

SIMS (Smart Irrigation Management System) is a backend application designed to manage IoT sensor data, control irrigation operations, and provide AI-driven irrigation recommendations. This project is built using Django and Django REST Framework.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and role management
- IoT sensor data management
- Irrigation schedule management
- AI-driven irrigation recommendations
- RESTful API endpoints

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/DulshanRerg/auto-irrigator.git
    cd sims_backend
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Configuration

Configure the environment variables in a `.env` file in the project root. Example:

```env
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
CORS_ALLOWED_ORIGINS=http://localhost:3000