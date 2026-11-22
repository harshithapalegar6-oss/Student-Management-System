import mysql.connector
import os

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("MYSQL_PASSWORD"),
            database="student_db"
        )
        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None