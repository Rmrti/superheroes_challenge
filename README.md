# 🚀 Superheroes Challenge

## 📌 Project Overview
Superheroes Challenge is a Flask-based web application that allows users to explore and manage a collection of superheroes and their powers. It follows a **many-to-many relationship**, where:  

- A **Hero** has many **Powers** through **HeroPower**  
- A **Power** has many **Heroes** through **HeroPower**  
- A **HeroPower** belongs to both a **Hero** and a **Power**  

The application is built using **Flask**, **SQLAlchemy**, **Alembic**, and **SQLite**.

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
✅ CRUD operations for **Heroes, Powers, and HeroPowers**  
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

### 🦸‍♂️ Hero Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/heroes` | Get all superheroes |
| **GET** | `/heroes/<id>` | Get a specific superhero by ID |
| **POST** | `/heroes` | Add a new superhero |
| **PUT** | `/heroes/<id>` | Update superhero details |


---

### ⚡ Power Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/powers` | Get all powers |
| **GET** | `/powers/<id>` | Get a specific power by ID |
| **POST** | `/powers` | Add a new power |
| **PUT** | `/powers/<id>` | Update power details |


---

### 🔗 HeroPower Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| **GET** | `/hero_powers` | Get all hero-power relationships |
| **GET** | `/hero_powers/<id>` | Get a specific hero-power relationship |
| **POST** | `/hero_powers` | Assign a power to a hero |
| **PUT** | `/hero_powers/<id>` | Update hero-power relationship |


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

🚀 Happy Coding! 🦸‍♂️🦸‍♀️⚡
