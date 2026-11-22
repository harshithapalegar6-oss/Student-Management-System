Student Management System

Project Overview

The Student Management System is a Python-based application that uses MySQL to store and manage student information.

It allows users to add, view, search, update, and delete student records. It also provides an option to export student details into a CSV file.

Technologies Used

- Python
- MySQL
- MySQL Connector
- CSV Module
- Object-Oriented Programming (OOP)

Features

1. Add new student records.
2. View all student records.
3. Search students by ID.
4. Search students by name.
5. Update student information.
6. Delete student records.
7. Prevent duplicate student IDs.
8. Export student records to CSV.

Database Structure

Database Name: "student_db"

Table Name: "students"

Column| Data Type
student_id| INT (Primary Key)
name| VARCHAR(100)
age| INT
department| VARCHAR(50)

Project Structure

StudentManagementSystem/
│
├── main.py
├── database.py
├── README.md
└── students.csv

Installation and Setup

1. Install Python.
2. Install MySQL Server.
3. Install the required Python package:

pip install mysql-connector-python

4. Create a MySQL database named "student_db".
5. Create the "students" table.
6. Update your MySQL connection settings in "database.py".
7. Run "main.py".

How to Run

python main.py

Learning Outcomes

- Python programming
- Object-Oriented Programming
- MySQL database connectivity
- CRUD operations
- SQL queries
- CSV file handling
- Input validation and exception handling

Author

Harshitha

Project Type

Academic / Personal Learning Project