# 🚀 Superheroes Challenge

## 📌 Project Overview
Superheroes Challenge is a Flask-based web application that allows users to explore and manage a collection of superheroes. It uses **Flask**, **SQLAlchemy**, **Alembic**, and **SQLite** for backend functionality.

---

## 📖 Table of Contents  
- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Database Migrations](#database-migrations)  
- [API Endpoints](#api-endpoints)  
- [Contributing](#contributing)  
- [License](#license)  

---

## 🎯 Features  
✅ Create, Read, Update, and Delete (CRUD) superheroes  
✅ SQLite database integration with Flask-SQLAlchemy  
✅ Alembic for database migrations  
✅ RESTful API with Flask  

---

## 🛠 Technologies Used  
- **Python 3.x**  
- **Flask** - Lightweight web framework  
- **Flask-SQLAlchemy** - ORM for database interaction  
- **Flask-Migrate** - Database migrations with Alembic  
- **SQLite** - Lightweight database  

---

## 🔧 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/your-username/superheroes_challenge.git
cd superheroes_challenge
```

### 2️⃣ Set Up a Virtual Environment  
```sh
python -m venv venv  
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up the Database  
```sh
flask db init  
flask db migrate -m "Initial migration"  
flask db upgrade  
```

---

## 🚀 Usage  

### Run the Application  
```sh
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser.

---

## 🔄 Database Migrations  

If you update your models, run:  
```sh
flask db migrate -m "Describe your changes"
flask db upgrade
```

---

## 🌐 API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/heroes` | Get all superheroes |
| **GET** | `/heroes/<id>` | Get a specific superhero by ID |
| **POST** | `/heroes` | Add a new superhero |
| **PUT** | `/heroes/<id>` | Update superhero details |
| **DELETE** | `/heroes/<id>` | Delete a superhero |

---

## 👥 Contributing  
Pull requests are welcome! Please follow these steps:  
1. **Fork** the repository  
2. **Create a new branch** (`feature-name`)  
3. **Commit changes** (`git commit -m "Add new feature"`)  
4. **Push to the branch** (`git push origin feature-name`)  
5. **Create a Pull Request**  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

🚀 Happy Coding! 🦸‍♂️🦸‍♀️
