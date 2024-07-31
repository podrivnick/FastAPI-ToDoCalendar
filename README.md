# FastAPI-ToDoCalendar

A non-commercial pet project that includes registration, authentication, authorization,
access to other users through a generated token,
task assignment to oneself and other users whose tokens have been previously connected.
The task includes text, a time limit, and an execution priority.

### Installation and Running

These instructions will help you run the project.

## Requirements

Ensure you have the following software installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [GNU Make](https://www.gnu.org/software/make/)

___
## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/podrivnick/FastAPI-ToDoCalendar.git
   cd FastAPI-ToDoCalendar 
   ```

2. Install all required packages in `Requirements` section.

### Implemented Commands

* `make app` - up application and database/infrastructure
* `make app-logs` - follow the logs in app container
* `make migrate` - apply all made migrations
* `make app-down` - down application and all infrastructure

### Specific Commands

* `make storages` - up only storages. you should run your application locally for debugging/developing purposes 
* `make storages-logs` - follow the logs in storages containers
* `make storages-down` - down all infrastructure
* `make appbash` - enter into application container

___
## Structure

```plaintext
ToDoProject/
    ├── .env.example               # Example environment variables file
    ├── .gitignore                 # Git ignore file
    ├── Dockerfile                 # Docker file for creating the application image
    ├── Makefile                   # Makefile for task automation
    ├── README.md                  # Project documentation
    ├── poetry.lock                # Poetry dependency lock file
    ├── pyproject.toml             # Poetry configuration file and dependencies
    ├── entrypoint.sh              # Docker container entry point
    ├── docker_compose/            # Docker Compose configurations
    │   ├── storages.yaml
    │   └── app.yaml
    └── src/                       # Main application source code
        ├── __init__.py
        ├── app.py                 # Main application file
        ├── config.py              # Application configuration
        ├── alembic.ini            # Alembic configuration for migrations
        ├── migrations/            # Alembic migrations
        │   ├── versions
        │   ├── __init__.py
        │   ├── env.py
        ├── database/              # Database module
        │   ├── __init__.py
        │   ├── database.py
        ├── services/              # Services and business logic
        │   ├── cookies_auth.py
        ├── schemas/               # Schemas to Models
        │   ├── calendar.py
        │   ├── users.py
        ├── models/                # All Models
        │   ├── __init__.py
        │   ├── calendar.py
        │   ├── users.py
        ├── utils/
        │   ├── manager.py         # Manager Authentication
        ├── api/                   # API routes
        │   ├── __init__.py
        │   ├── users.py
        │   ├── routers.py
        ├── tests/                 # Tests
        │   ├── __init__.py
        └── front/                 # Frontend resources
            ├── static/            # Static files
            │   ├── css/
            │   ├── js/
            │   └── img/
            └── templates/         # Jinja2 templates
                └── html/
                    ├── base.html
                    └── user_profile.html
```

## Technology
+ **FastAPI**
+ **Python**
+ **JavaScript**

___
## Design Patterns
+ **MVT** (Model-View-Template): 
  + ***Model***: Represents the data and business logic of the project.
  + ***View***: Handles the requests and sends the response to the user.
  + ***Template***: Defines what data is sent to the user.
+ **Authentication and Authorization** (JWT)
+ **Repository Pattern**
+ **Configuration Management** (dotenv)
+ **Factory Pattern**
+ **Dependency Injection**: (Depends)

## Author
Author of the backend: ***Rybakov Artem***  (https://github.com/podrivnick)   

Author of the frontend-calendar: **https://github.com/opensource-coding/Responsive-Calendar-with-Events**