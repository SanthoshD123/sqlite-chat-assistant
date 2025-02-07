import os
import sqlite3
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
DB_PATH = 'database.db'


def execute_query(query, params=()):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        print(f"Database Error: {e}")
        return []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def handle_query():
    user_input = request.form.get('user_input', '').strip()

    # Comprehensive query handling
    try:
        if "all employees in" in user_input.lower():
            department = user_input.split("in ")[-1].strip()
            query = "SELECT Name FROM Employees WHERE UPPER(Department) = UPPER(?)"
            result = execute_query(query, (department,))
            response = [f"Employee: {row[0]}" for row in result] or ["No employees found."]

        elif "manager of" in user_input.lower():
            department = user_input.split("of ")[-1].strip()
            query = "SELECT Manager FROM Departments WHERE UPPER(Name) = UPPER(?)"
            result = execute_query(query, (department,))
            response = [f"The manager of {department} is {row[0]}" for row in result] or ["No manager found."]

        elif "hired after" in user_input.lower():
            date = user_input.split("after ")[-1].strip()
            query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
            result = execute_query(query, (date,))
            response = [f"Employee: {row[0]}" for row in result] or ["No employees found."]

        elif "total salary expense for" in user_input.lower():
            department = user_input.split("for ")[-1].strip()
            query = "SELECT SUM(Salary) FROM Employees WHERE UPPER(Department) = UPPER(?)"
            result = execute_query(query, (department,))
            response = [f"Total salary expense for {department}: {result[0][0]}" if result and result[0][
                0] is not None else "No salary data found."]

        else:
            response = ["Sorry, I don't understand that query."]

        return jsonify(response)

    except Exception as e:
        return jsonify([f"Error processing query: {str(e)}"])


if __name__ == '__main__':
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary REAL,
            Hire_Date TEXT
        )''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Manager TEXT NOT NULL
        )''')

        # Insert sample data
        cursor.executemany('INSERT OR REPLACE INTO Employees VALUES (?, ?, ?, ?, ?)', [
            (1, 'Alice', 'Sales', 50000, '2021-01-15'),
            (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
            (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
        ])

        cursor.executemany('INSERT OR REPLACE INTO Departments VALUES (?, ?, ?)', [
            (1, 'Sales', 'Alice'),
            (2, 'Engineering', 'Bob'),
            (3, 'Marketing', 'Charlie')
        ])

        conn.commit()
        conn.close()

    app.run(debug=True)