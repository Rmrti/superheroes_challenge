

---

# Superheroes API

This is a Flask-based API for managing superheroes, their powers, and the relationships between them. The application allows users to create heroes, powers, and manage their abilities using a simple, RESTful interface. The backend is built with Flask and SQLAlchemy, and it supports relational data models for heroes and their powers.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [POST /heroes](#post-heroes)
  - [POST /powers](#post-powers)
  - [GET /heroes](#get-heroes)
  - [GET /powers](#get-powers)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides an API for managing superheroes and their superpowers. The application is designed to handle CRUD (Create, Read, Update, Delete) operations for heroes and powers, using Flask as the backend framework and SQLAlchemy for database management. The models include `Hero`, `Power`, and `HeroPower`, representing the superheroes, their powers, and the association between them.

## Features

- **Create Hero**: Create a new hero with a name and superpower identity.
- **Create Power**: Add new powers with descriptions to the system.
- **View All Heroes**: List all superheroes with their details.
- **View All Powers**: List all powers with descriptions.
- **Associate Powers with Heroes**: Link a hero to specific powers through the `HeroPower` relationship.

## Tech Stack

- **Flask**: Web framework used to create the API.
- **SQLAlchemy**: ORM for interacting with the SQLite database.
- **SQLite**: Lightweight database to store hero and power data.
- **Postman/HTTP Client**: For testing and interacting with API endpoints.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/superheroes-api.git
   cd superheroes-api
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Run the following command to initialize the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

   The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### POST /heroes

Create a new hero.

**Request Body**:
```json
{
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel"
}
```

### POST /powers

Create a new superpower.

**Request Body**:
```json
{
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

**Response**:
```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

### GET /heroes

Retrieve a list of all heroes.

**Response**:
```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  {
    "id": 2,
    "name": "Doreen Green",
    "super_name": "Squirrel Girl"
  }
]
```

### GET /powers

Retrieve a list of all powers.

**Response**:
```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  },
  {
    "id": 2,
    "name": "flight",
    "description": "gives the wielder the ability to fly through the skies at supersonic speed"
  }
]
```

## Testing

To test the API, you can use a tool like Postman or curl to interact with the endpoints. Here are some example commands for testing the `POST` and `GET` routes using `curl`.

- **Create a Hero**:
  ```bash
  curl -X POST http://127.0.0.1:5000/heroes -H "Content-Type: application/json" -d '{"name": "Kamala Khan", "super_name": "Ms. Marvel"}'
  ```

- **Create a Power**:
  ```bash
  curl -X POST http://127.0.0.1:5000/powers -H "Content-Type: application/json" -d '{"name": "super strength", "description": "gives the wielder super-human strengths"}'
  ```

- **Get All Heroes**:
  ```bash
  curl http://127.0.0.1:5000/heroes
  ```

## Contributing

Contributions to this project are welcome! Please fork the repository, create a new branch, and submit a pull request with your changes.

1. Fork the project
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adapt and expand this README as your project evolves!
