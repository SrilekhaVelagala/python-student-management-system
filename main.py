import sys
import database

def get_valid_int(prompt, min_val=None, max_val=None):
    """
    Helper function to safely get an integer input from the user.
    Prevents the program from crashing if a non-integer is entered.
    """
    while True:
        try:
            value = int(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Invalid input! Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Invalid input! Value cannot exceed {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def get_valid_float(prompt, min_val=None, max_val=None):
    """
    Helper function to safely get a float input (decimal) from the user.
    Used for CGPA input validation.
    """
    while True:
        try:
            value = float(input(prompt).strip())
            if min_val is not None and value < min_val:
                print(f"Invalid input! Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Invalid input! Value cannot exceed {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")

def get_valid_string(prompt):
    """
    Helper function to get a non-empty string input.
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Invalid input! This field cannot be empty.")
            continue
        return value

def display_menu():
    """
    Displays the user interface options menu.
    """
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM (MySQL)      ")
    print("=" * 45)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Details")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)

def format_student_table(students):
    """
    Prints a list of students in a well-formatted console table.
    """
    # Header format: ID is 10 chars, Name is 20, Age is 6, Branch is 15, CGPA is 6
    header_format = "| {:<10} | {:<20} | {:<6} | {:<15} | {:<6} |"
    divider = "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*8 + "+" + "-"*17 + "+" + "-"*8 + "+"
    
    print(divider)
    print(header_format.format("ID", "Name", "Age", "Branch", "CGPA"))
    print(divider)
    for student in students:
        # student tuple structure: (student_id, name, age, branch, cgpa)
        print(header_format.format(student[0], student[1], student[2], student[3], float(student[4])))
    print(divider)

def handle_add_student():
    print("\n--- Add Student Record ---")
    
    # 1. Input and Validate Student ID
    student_id = get_valid_int("Enter Student ID (Numbers only): ", min_val=1)
    
    # 2. Check if the Student ID already exists in the database
    existing_student = database.search_student(student_id)
    if existing_student:
        print(f"\n[Warning] A student with ID {student_id} already exists!")
        return

    # 3. Input other student fields
    name = get_valid_string("Enter Student Name: ")
    age = get_valid_int("Enter Age (15 - 100): ", min_val=15, max_val=100)
    branch = get_valid_string("Enter Branch (e.g. CSE, ECE, EEE): ")
    cgpa = get_valid_float("Enter CGPA (0.00 - 10.00): ", min_val=0.0, max_val=10.0)

    # 4. Insert into MySQL Database
    database.add_student(student_id, name, age, branch, cgpa)

def handle_view_students():
    print("\n--- View All Students ---")
    students = database.view_all_students()
    
    if not students:
        print("No student records found in the database.")
    else:
        # Print the total count of students
        print(f"Total Students: {len(students)}")
        format_student_table(students)

def handle_search_student():
    print("\n--- Search Student by ID ---")
    student_id = get_valid_int("Enter Student ID to Search: ", min_val=1)
    
    # Search in database
    student = database.search_student(student_id)
    
    if student:
        print("\nStudent Record Found:")
        # We pass it as a list to our table formatter
        format_student_table([student])
    else:
        print(f"\n[Warning] Student with ID {student_id} not found.")

def handle_update_student():
    print("\n--- Update Student Details ---")
    student_id = get_valid_int("Enter Student ID to Update: ", min_val=1)
    
    # Search if the student exists before asking for details
    student = database.search_student(student_id)
    
    if not student:
        print(f"\n[Warning] Student with ID {student_id} not found.")
        return

    # Unpack current details
    # student = (student_id, current_name, current_age, current_branch, current_cgpa)
    curr_id, curr_name, curr_age, curr_branch, curr_cgpa = student
    
    print(f"\nCurrent Details:")
    print(f"Name: {curr_name} | Age: {curr_age} | Branch: {curr_branch} | CGPA: {curr_cgpa}")
    print("\n(Press ENTER to keep the current value unchanged)")

    # Read inputs and fall back to current values if user presses ENTER
    # 1. Update Name
    name_input = input(f"Enter New Name [{curr_name}]: ").strip()
    new_name = name_input if name_input else curr_name

    # 2. Update Age
    while True:
        age_input = input(f"Enter New Age [{curr_age}]: ").strip()
        if not age_input:
            new_age = curr_age
            break
        try:
            new_age = int(age_input)
            if 15 <= new_age <= 100:
                break
            print("Invalid input! Age must be between 15 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    # 3. Update Branch
    branch_input = input(f"Enter New Branch [{curr_branch}]: ").strip()
    new_branch = branch_input if branch_input else curr_branch

    # 4. Update CGPA
    while True:
        cgpa_input = input(f"Enter New CGPA [{curr_cgpa}]: ").strip()
        if not cgpa_input:
            new_cgpa = float(curr_cgpa)
            break
        try:
            new_cgpa = float(cgpa_input)
            if 0.0 <= new_cgpa <= 10.0:
                break
            print("Invalid input! CGPA must be between 0.00 and 10.00.")
        except ValueError:
            print("Invalid input! Please enter a valid decimal number.")

    # Save changes to the database
    database.update_student(student_id, new_name, new_age, new_branch, new_cgpa)

def handle_delete_student():
    print("\n--- Delete Student Record ---")
    student_id = get_valid_int("Enter Student ID to Delete: ", min_val=1)
    
    # Search first to show student detail and confirm
    student = database.search_student(student_id)
    if not student:
        print(f"\n[Warning] Student with ID {student_id} not found.")
        return
        
    print("\nStudent details to be deleted:")
    format_student_table([student])
    
    # Double check delete decision
    confirm = input("Are you sure you want to delete this student? (y/n): ").strip().lower()
    if confirm == 'y':
        database.delete_student(student_id)
    else:
        print("\nDeletion cancelled.")

def main():
    """
    Main application runner loop.
    """
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            handle_add_student()
        elif choice == "2":
            handle_view_students()
        elif choice == "3":
            handle_search_student()
        elif choice == "4":
            handle_update_student()
        elif choice == "5":
            handle_delete_student()
        elif choice == "6":
            print("\nThank you for using the Student Management System. Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice! Please choose a option from 1 to 6.")

# Execution entry point
if __name__ == "__main__":
    main()
