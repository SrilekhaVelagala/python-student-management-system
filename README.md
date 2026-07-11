# Student Management System

A beginner-friendly, console-based **Student Management System** built using **Python** and **MySQL**. This project is designed specifically for academic evaluation (e.g., B.Tech lab examinations/projects) and interviews. It demonstrates basic database operations, exception handling, data verification, and console user interface design without using overly complex programming concepts.

---

## Folder Structure

```text
Student Management System/
│
├── schema.sql           # Database creation & table setup script
├── database.py         # MySQL connection setup & CRUD operation functions
├── main.py             # CLI menu-driven user interface and validation logic
├── requirements.txt    # Required python dependencies (mysql-connector-python)
└── README.md           # Project documentation and guide
```

---

## Features

1. **Add Student**: Allows adding new student records containing:
   - Student ID (must be a unique number)
   - Name (cannot be empty)
   - Age (validated between 15 and 100)
   - Branch (e.g., CSE, ECE, EEE)
   - CGPA (validated between 0.00 and 10.00)
2. **View All Students**: Retrieves all records from the database and displays them in a neatly aligned grid table.
3. **Search Student by ID**: Searches for a student by their ID and displays their details.
4. **Update Student Details**: Allows modifying the details of an existing student. Pressing `ENTER` on any input prompts keeps its current value unchanged.
5. **Delete Student**: Safely deletes a student record after displaying the record and asking for confirmation.
6. **Robust Input Validation**: Safely handles inputs to prevent crashes when invalid data formats (e.g., alphabetical characters instead of numbers/CGPA) are entered.

---

## Technologies Used

- **Python 3.x**: Programming language for application logic.
- **MySQL**: Relational database management system for persistent data storage.
- **mysql-connector-python**: Official driver to connect Python with the MySQL database.

---

## Database Schema

The system uses a database named `student_db` containing a single table `students` defined as follows:

| Column Name  | Data Type     | Constraints                  | Description                          |
|:-------------|:--------------|:-----------------------------|:-------------------------------------|
| `student_id` | `INT`         | `PRIMARY KEY`                | Unique identifier for each student   |
| `name`       | `VARCHAR(100)`| `NOT NULL`                   | Name of the student (mandatory)      |
| `age`        | `INT`         | -                            | Student's age (e.g., 18, 20)         |
| `branch`     | `VARCHAR(50)` | -                            | Department (e.g., CSE, IT)           |
| `cgpa`       | `DECIMAL(3,2)`| -                            | Cumulative Grade Point Average       |

---

## How to Setup and Run the Project

### Step 1: Pre-requisites
1. **Python**: Make sure Python 3.x is installed on your computer.
2. **MySQL**: Make sure you have MySQL Server installed and running locally.

### Step 2: Install Dependencies
Open your command prompt or terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### Step 3: Setup the Database
1. Open your MySQL Command Line Client or any tool like MySQL Workbench/phpMyAdmin.
2. Log in using your root or user credentials.
3. Run the SQL script from `schema.sql` to create the database and table:
   ```sql
   SOURCE schema.sql;
   ```
   *(Alternatively, you can copy the contents of `schema.sql` and run them inside your MySQL client).*

### Step 4: Configure database.py
Open `database.py` in your text editor and modify the configuration variables at the top of the file to match your MySQL server login credentials:
```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_actual_password_here"  # Update this with your database password
DB_NAME = "student_db"
```

### Step 5: Run the Application
Start the application from your terminal:
```bash
python main.py
```

---

## Sample Screenshots (How to Add)

To add screenshots to your project submission:
1. Create a folder named `assets` in the project root directory.
2. Take screenshots of each operation (e.g., Main Menu, Add Student success, View Table) when running the application.
3. Save the screenshots inside the `assets/` folder (e.g., `assets/main_menu.png`, `assets/view_students.png`).
4. Link them in this file using the Markdown format:
   ```markdown
   ![Main Menu](assets/main_menu.png)
   ![View Students](assets/view_students.png)
   ```

*(Example placeholders below)*

### 1. Main Menu Interface
*(Take a screenshot of the initial menu and insert it here)*
<!-- Replace this placeholder with: ![Main Menu](assets/main_menu.png) -->

### 2. View Students Table
*(Take a screenshot of the grid table output when viewing students and insert it here)*
<!-- Replace this placeholder with: ![View Students](assets/view_students.png) -->

### 3. Search and Update Operations
*(Take a screenshot of the search or update student execution and insert it here)*
<!-- Replace this placeholder with: ![Update Student](assets/update_student.png) -->
