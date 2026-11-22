import mysql.connector
import csv
from database import connect_db


# Student Class
class Student:

    def __init__(self, student_id, name, age, department):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)


# Student Management System
class StudentManagementSystem:

    # 1. Add Student
    def add_student(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("Invalid Student ID!")
                return

            cursor.execute(
                "SELECT student_id FROM students WHERE student_id = %s",
                (student_id,)
            )

            if cursor.fetchone():
                print("This Student ID already exists!")
                return

            name = input("Enter Student Name: ").strip()

            if not name:
                print("Name cannot be empty!")
                return

            age = int(input("Enter Age: "))

            if age <= 0:
                print("Invalid Age!")
                return

            department = input("Enter Department: ").strip()

            if not department:
                print("Department cannot be empty!")
                return

            student = Student(student_id, name, age, department)

            query = """
            INSERT INTO students
            (student_id, name, age, department)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    student.student_id,
                    student.name,
                    student.age,
                    student.department
                )
            )

            db.commit()
            print("Student added successfully!")

        except ValueError:
            print("Please enter valid numbers.")

        except mysql.connector.Error as error:
            db.rollback()
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 2. View Students
    def view_students(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()

            if records:
                print("\n===== STUDENT DETAILS =====")

                for record in records:
                    student = Student(
                        record[0],
                        record[1],
                        record[2],
                        record[3]
                    )

                    print("----------------------")
                    student.display_details()

            else:
                print("No student records found.")

        except mysql.connector.Error as error:
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 3. Search Student by ID
    def search_student(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM students WHERE student_id = %s",
                (student_id,)
            )

            record = cursor.fetchone()

            if record:
                student = Student(*record)
                print("\n===== STUDENT FOUND =====")
                student.display_details()

            else:
                print("Student not found.")

        except ValueError:
            print("Please enter a valid Student ID.")

        except mysql.connector.Error as error:
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 4. Search Student by Name
    def search_by_name(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            name = input("Enter Student Name: ").strip()

            if not name:
                print("Name cannot be empty!")
                return

            cursor.execute(
                "SELECT * FROM students WHERE name LIKE %s",
                ("%" + name + "%",)
            )

            records = cursor.fetchall()

            if records:
                print("\n===== SEARCH RESULTS =====")

                for record in records:
                    student = Student(*record)
                    print("----------------------")
                    student.display_details()

            else:
                print("No matching student found.")

        except mysql.connector.Error as error:
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 5. Update Student
    def update_student(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM students WHERE student_id = %s",
                (student_id,)
            )

            if cursor.fetchone() is None:
                print("Student not found.")
                return

            name = input("Enter New Name: ").strip()

            if not name:
                print("Name cannot be empty!")
                return

            age = int(input("Enter New Age: "))

            if age <= 0:
                print("Invalid Age!")
                return

            department = input("Enter New Department: ").strip()

            if not department:
                print("Department cannot be empty!")
                return

            cursor.execute(
                """
                UPDATE students
                SET name = %s, age = %s, department = %s
                WHERE student_id = %s
                """,
                (name, age, department, student_id)
            )

            db.commit()
            print("Student updated successfully!")

        except ValueError:
            print("Please enter valid numbers.")

        except mysql.connector.Error as error:
            db.rollback()
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 6. Delete Student
    def delete_student(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            student_id = int(input("Enter Student ID: "))

            cursor.execute(
                "SELECT * FROM students WHERE student_id = %s",
                (student_id,)
            )

            if cursor.fetchone() is None:
                print("Student not found.")
                return

            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirm == "yes":

                cursor.execute(
                    "DELETE FROM students WHERE student_id = %s",
                    (student_id,)
                )

                db.commit()
                print("Student deleted successfully!")

            else:
                print("Delete cancelled.")

        except ValueError:
            print("Please enter a valid Student ID.")

        except mysql.connector.Error as error:
            db.rollback()
            print("Database error:", error)

        finally:
            cursor.close()
            db.close()

    # 7. Export Students to CSV
    def export_to_csv(self):

        db = connect_db()
        if db is None:
            return

        cursor = db.cursor()

        try:
            cursor.execute("SELECT * FROM students")
            records = cursor.fetchall()

            if not records:
                print("No student records available to export.")
                return

            with open(
                "students.csv",
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Student ID",
                    "Name",
                    "Age",
                    "Department"
                ])

                writer.writerows(records)

            print("Student records exported successfully!")
            print("File name: students.csv")

        except mysql.connector.Error as error:
            print("Database error:", error)

        except OSError as error:
            print("File error:", error)

        finally:
            cursor.close()
            db.close()

    # Main Menu
    def menu(self):

        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student by ID")
            print("4. Search Student by Name")
            print("5. Update Student")
            print("6. Delete Student")
            print("7. Export Students to CSV")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.search_by_name()

            elif choice == "5":
                self.update_student()

            elif choice == "6":
                self.delete_student()

            elif choice == "7":
                self.export_to_csv()

            elif choice == "8":
                print("Thank you for using Student Management System!")
                break

            else:
                print("Invalid choice! Please select 1 to 8.")


# Start Application
if __name__ == "__main__":

    app = StudentManagementSystem()
    app.menu()