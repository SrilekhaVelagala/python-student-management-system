import mysql.connector
from mysql.connector import Error

# Database connection configuration
# You can change these details according to your local MySQL server setup
DB_HOST = "localhost"
DB_USER = "root"
# Make sure to update the password to your local MySQL password
DB_PASSWORD = "password"
DB_NAME = "student_db"

def get_connection():
    """
    Establishes a connection to the MySQL database.
    Returns:
        connection object if successful, None otherwise.
    """
    try:
        # Establish connection with host, user, password, and database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Error as e:
        # Print database connection error if database does not exist or credentials are wrong
        print(f"\n[Error] Database Connection Failed: {e}")
        print("Please ensure your MySQL server is running and configuration in 'database.py' is correct.")
        return None

def add_student(student_id, name, age, branch, cgpa):
    """
    Adds a new student record to the 'students' table.
    
    SQL Query Explained:
        INSERT INTO students (student_id, name, age, branch, cgpa) VALUES (%s, %s, %s, %s, %s)
        - 'INSERT INTO students' specifies that we are adding a record to the 'students' table.
        - The column names are specified in parentheses.
        - '%s' acts as placeholders (parameterized query) which prevents SQL injection attacks 
          and handles data type formatting automatically.
    """
    connection = get_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "INSERT INTO students (student_id, name, age, branch, cgpa) VALUES (%s, %s, %s, %s, %s)"
    values = (student_id, name, age, branch, cgpa)
    
    try:
        # Execute the SQL query with the provided student values
        cursor.execute(query, values)
        # Commit the transaction to save changes permanently in the database
        connection.commit()
        print("\n[Success] Student added successfully!")
        return True
    except Error as e:
        # Rollback in case of error to maintain database integrity
        connection.rollback()
        # Handle cases like duplicate Student ID (Primary Key violation)
        if e.errno == 1062:
            print(f"\n[Error] Student with ID {student_id} already exists.")
        else:
            print(f"\n[Error] Failed to add student: {e}")
        return False
    finally:
        # Close the cursor and connection resources to prevent memory leaks
        cursor.close()
        connection.close()

def view_all_students():
    """
    Fetches all student records from the 'students' table.
    
    SQL Query Explained:
        SELECT student_id, name, age, branch, cgpa FROM students
        - 'SELECT' retrieves specified columns.
        - 'FROM students' indicates the table from which data should be fetched.
    """
    connection = get_connection()
    if connection is None:
        return []
    
    cursor = connection.cursor()
    query = "SELECT student_id, name, age, branch, cgpa FROM students"
    
    try:
        # Execute the SELECT query
        cursor.execute(query)
        # Fetch all matching rows of the query result
        students = cursor.fetchall()
        return students
    except Error as e:
        print(f"\n[Error] Failed to fetch students: {e}")
        return []
    finally:
        # Close connection resources
        cursor.close()
        connection.close()

def search_student(student_id):
    """
    Searches for a student by their unique Student ID.
    
    SQL Query Explained:
        SELECT student_id, name, age, branch, cgpa FROM students WHERE student_id = %s
        - 'WHERE student_id = %s' filters the search to only return the record 
          matching the given student_id.
    """
    connection = get_connection()
    if connection is None:
        return None
    
    cursor = connection.cursor()
    query = "SELECT student_id, name, age, branch, cgpa FROM students WHERE student_id = %s"
    
    try:
        # Execute the parameterized search query
        cursor.execute(query, (student_id,))
        # Fetch a single matching record
        student = cursor.fetchone()
        return student
    except Error as e:
        print(f"\n[Error] Failed to search student: {e}")
        return None
    finally:
        # Close resources
        cursor.close()
        connection.close()

def update_student(student_id, name, age, branch, cgpa):
    """
    Updates the details of an existing student in the database.
    
    SQL Query Explained:
        UPDATE students SET name = %s, age = %s, branch = %s, cgpa = %s WHERE student_id = %s
        - 'UPDATE students' specifies the table name to modify.
        - 'SET' defines the column values to update.
        - 'WHERE student_id = %s' restricts the update to only the specific student's record.
    """
    connection = get_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "UPDATE students SET name = %s, age = %s, branch = %s, cgpa = %s WHERE student_id = %s"
    values = (name, age, branch, cgpa, student_id)
    
    try:
        # Execute update query
        cursor.execute(query, values)
        # Commit changes to apply updates to the database
        connection.commit()
        # rowcount represents how many rows were modified
        if cursor.rowcount > 0:
            print("\n[Success] Student details updated successfully!")
            return True
        else:
            print("\n[Warning] No student found with that ID or details are unchanged.")
            return False
    except Error as e:
        connection.rollback()
        print(f"\n[Error] Failed to update student details: {e}")
        return False
    finally:
        # Close resources
        cursor.close()
        connection.close()

def delete_student(student_id):
    """
    Removes a student record from the 'students' table.
    
    SQL Query Explained:
        DELETE FROM students WHERE student_id = %s
        - 'DELETE FROM students' specifies that records are being removed from the 'students' table.
        - 'WHERE student_id = %s' ensures only the student with the matching ID is deleted.
          (WARNING: If WHERE is omitted, all records in the table will be deleted!)
    """
    connection = get_connection()
    if connection is None:
        return False
    
    cursor = connection.cursor()
    query = "DELETE FROM students WHERE student_id = %s"
    
    try:
        # Execute the delete query
        cursor.execute(query, (student_id,))
        connection.commit()
        
        # Check if a row was actually deleted
        if cursor.rowcount > 0:
            print(f"\n[Success] Student with ID {student_id} deleted successfully.")
            return True
        else:
            print(f"\n[Warning] No student found with ID {student_id}.")
            return False
    except Error as e:
        connection.rollback()
        print(f"\n[Error] Failed to delete student: {e}")
        return False
    finally:
        # Close resources
        cursor.close()
        connection.close()
