from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",  # Change if using a different MySQL user
        password="68311380",  # Use your actual MySQL password
        database="academic_record_db"
    )

# Home page – View all students
@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", students=students)

# Add new student
@app.route("/add-student", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        enrollment_date = request.form["enrollment_date"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")
    return render_template("add_student.html")

# Delete student
@app.route("/delete-student/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE student_id = %s", (student_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/")

@app.route("/edit-student/<int:student_id>", methods=["GET", "POST"])
def edit_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        enrollment_date = request.form["enrollment_date"]

        cursor.execute("""
            UPDATE Students
            SET first_name = %s, last_name = %s, email = %s, enrollment_date = %s
            WHERE student_id = %s
        """, (first_name, last_name, email, enrollment_date, student_id))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/")

    cursor.execute("SELECT * FROM Students WHERE student_id = %s", (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit_student.html", student=student)


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
