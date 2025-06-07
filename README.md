## Overview

**Project Title**:  
**Course Management Portal**

**Project Description**:  
This web application allows users to manage student data in a university-style system. Users can view, add, update, and delete student records stored in a MySQL database. The app uses Flask for routing and rendering and connects directly to a SQL-based academic record system built in a previous sprint.

**Project Goals**:  
- Build a web interface for SQL-based student registration data  
- Practice full CRUD (Create, Read, Update, Delete) operations  
- Integrate frontend and backend systems using Flask  
- Design a functional and user-friendly interface for course record management

---

## Instructions for Build and Use

### Steps to build and/or run the software:

1. Clone the GitHub repository.
2. Make sure MySQL is running and the `academic_record_db` is created with required tables (see `CSE 310.sql`).
3. Run the Flask app with `python app.py`.

### Instructions for using the software:

1. Go to `http://127.0.0.1:5000` in your browser.
2. Use the "➕ Add New Student" button to insert new student records.
3. Use the "✏️ Edit" or "Delete" buttons to update or remove existing students.
4. Use the search bar to filter through records by name or email.

---

## Development Environment 

To recreate the development environment, you need the following software and libraries:

* Python 3.12+
* Flask 2.3+
* MySQL 8.x
* mysql-connector-python
* MySQL Workbench or DBeaver (for viewing DB)
* VS Code (recommended code editor)

---

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Flask Documentation](https://flask.palletsprojects.com/)
* [W3Schools HTML/CSS/JS](https://www.w3schools.com/)
* [Traversy Media - Flask & MySQL Crash Course](https://www.youtube.com/@TraversyMedia)
* [MySQL Official Docs](https://dev.mysql.com/doc/)

---

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add user login and authentication with session storage
* [ ] Create student enrollment linking to courses and instructors
* [ ] Export data as CSV or PDF

