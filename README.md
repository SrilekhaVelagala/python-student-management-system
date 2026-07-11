# 🎓 Student Management System

A beginner-friendly **Student Management System** developed using **Python** and **MySQL**. This is a console-based application that performs CRUD (Create, Read, Update, Delete) operations on student records. The project demonstrates Python programming, database connectivity, input validation, and SQL queries.

---

## 📌 Features

- ➕ Add a new student
- 📋 View all student records
- 🔍 Search a student by ID
- ✏️ Update student details
- ❌ Delete a student record
- ✅ Input validation for ID, Age, and CGPA
- 🔒 Uses parameterized SQL queries to improve security

---

## 🛠️ Technologies Used

- Python 3
- MySQL
- MySQL Connector for Python (`mysql-connector-python`)
- SQL

---

## 📂 Project Structure

```text
Student Management System/
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

Database Name:

```
student_db
```

Table:

```
students
```

| Column | Data Type | Constraint |
|---------|----------|------------|
| student_id | INT | PRIMARY KEY |
| name | VARCHAR(100) | NOT NULL |
| age | INT | - |
| branch | VARCHAR(50) | - |
| cgpa | DECIMAL(3,2) | - |

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/SrilekhaVelagala/python-student-management-system.git
```

### 2. Navigate to the project folder

```bash
cd python-student-management-system
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

Open MySQL and run:

```sql
SOURCE schema.sql;
```

Or copy and execute the SQL statements from `schema.sql`.

### 5. Configure database connection

Open `database.py` and update the following values according to your MySQL installation.

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_NAME = "student_db"
```

### 6. Run the project

```bash
python main.py
```

---

## 💻 Application Workflow

1. User selects an option from the menu.
2. The application validates the input.
3. Python connects to the MySQL database.
4. SQL queries are executed.
5. Results are displayed in a formatted table.

---

## 📚 Concepts Demonstrated

- Python Functions
- Exception Handling
- Input Validation
- MySQL Database Connectivity
- CRUD Operations
- Parameterized SQL Queries
- Modular Programming

---

## 🚀 Future Improvements

- Search students by name
- Export records to CSV
- User authentication
- Graphical User Interface (Tkinter)
- Attendance management

---

## 👨‍💻 Author

**Srilekha Reddy**

B.Tech Computer Science Student

GitHub: https://github.com/SrilekhaVelagala

---

## ⭐ If you found this project helpful

If you like this project, consider giving it a ⭐ on GitHub.