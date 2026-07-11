-- ==========================================
-- SQL Script to Setup Student Management DB
-- ==========================================

-- 1. Create the Database if it does not already exist
CREATE DATABASE IF NOT EXISTS student_db;

-- 2. Switch to using the created database
USE student_db;

-- 3. Create the 'students' table to store student records
-- We define fields with suitable constraints:
--   - student_id: Unique integer entered by the user (Primary Key)
--   - name: Name of the student (cannot be empty)
--   - age: Age as a simple integer
--   - branch: Branch/Department (e.g., CSE, ECE, ME)
--   - cgpa: Cumulative Grade Point Average (Format: X.XX, max 10.00)
CREATE TABLE IF NOT EXISTS students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    branch VARCHAR(50),
    cgpa DECIMAL(3, 2)
);
