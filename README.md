# 🎓 Student Management System

A console-based **Student Management System** built with **Python** and **MySQL** as a mini project to practise connecting Python applications to a relational database. It performs CRUD (Create, Read, Update, Delete) operations on student records through a simple menu-driven interface.

---

## 📖 Project Overview

The application lets a user manage student records from the terminal: add new students, view all records, search by ID, update details, and delete records. User input is validated before it reaches the database, and all SQL queries are parameterized.

I built this project to get hands-on experience with Python functions, exception handling, MySQL connectivity, and writing SQL from application code, while keeping the user interface (`main.py`) separate from the database logic (`database.py`).

---

## ✨ Features

- ➕ Add a new student
- 📋 View all student records
- 🔍 Search a student by ID
- ✏️ Update student details
- ❌ Delete a student record
- ✅ Input validation for ID, Age, and CGPA
- 🔒 Parameterized SQL queries to help prevent SQL injection

---

## 🛠️ Technologies Used

| Technology                | Purpose                                  |
| ------------------------- | ---------------------------------------- |
| Python 3                  | Programming language                     |
| MySQL                     | Relational database                      |
| mysql-connector-python    | Connecting Python to MySQL               |
| SQL                       | Creating tables and querying data        |

---

## 📂 Project Structure

```
python-student-management-system/
│
├── database.py          # Database connection and CRUD operations
├── main.py              # Menu-driven console application
├── schema.sql           # Database and table creation script
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore
```

---

## 🗄️ Database Schema

**Database:** `student_db`
**Table:** `students`

| Column      | Data Type    | Constraint  |
| ----------- | ------------ | ----------- |
| student_id  | INT          | PRIMARY KEY |
| name        | VARCHAR(100) | NOT NULL    |
| age         | INT          | -           |
| branch      | VARCHAR(50)  | -           |
| cgpa        | DECIMAL(3,2) | -           |

---

## 💻 Application Workflow

1. The user selects an option from the menu.
2. The application validates the input.
3. Python connects to the MySQL database.
4. The SQL query is executed with parameters.
5. Results are displayed in a formatted table.

---

## 📚 What I Learned

- Writing modular Python code by separating UI logic from database logic
- Connecting Python to MySQL using `mysql-connector-python`
- Performing **CRUD operations** with SQL (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Using **parameterized queries** to avoid SQL injection
- Validating user input and handling errors with **exception handling**
- Designing a simple table with a **primary key**, constraints, and suitable data types (e.g., `DECIMAL` for CGPA)
- Committing transactions and managing database connections

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/SrilekhaVelagala/python-student-management-system.git
```

### 2. Navigate to the project folder

```
cd python-student-management-system
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Create the database

Open MySQL and run:

```
SOURCE schema.sql;
```

Or copy and execute the SQL statements from `schema.sql`.

### 5. Configure the database connection

Open `database.py` and update these values to match your MySQL setup:

```
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_NAME = "student_db"
```

> ⚠️ Do not commit your real password to GitHub.

### 6. Run the project

```
python main.py
```

---

## 🚀 Future Improvements

- Search students by name
- Export records to CSV
- Store database credentials in environment variables instead of the source file
- User authentication
- Graphical User Interface (Tkinter)
- Attendance management
- Unit tests for the database functions

---

## 👩‍💻 Author

**Srilekha Reddy**
B.Tech Computer Science Student
GitHub: <https://github.com/SrilekhaVelagala>

---

## 📄 License

This project was created for learning purposes.
