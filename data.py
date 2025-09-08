import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="Tayyab",
        password="1234",
        database="student_db",
    )

def enter_student(name,age,course):
    conn = get_connection()
    cursor = conn.cursor()
    query="INSERT INTO students (name, age, course) VALUES (%s,%s,%s)"
    cursor.execute (query, (name,age,course))
    conn.commit()
    conn.close()

def get_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(std_id):
    conn =get_connection()
    cursor =conn.cursor()
    query="DELETE FROM students WHERE std_id = %s"
    cursor.execute (query, (std_id,))
    conn.commit()
    conn.close()
