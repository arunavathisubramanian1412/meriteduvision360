from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            dob TEXT,
            gender TEXT,
            community TEXT,
            student_mobile TEXT,
            email TEXT,
            father_name TEXT,
            parent_mobile TEXT,
            address TEXT,
            district TEXT,
            pincode TEXT,
            mark10 TEXT,
            per10 TEXT,
            mark12 TEXT,
            per12 TEXT,
            selected_course TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.form
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applications (
                student_name, dob, gender, community, student_mobile, email, 
                father_name, parent_mobile, address, district, pincode, 
                mark10, per10, mark12, per12, selected_course
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('student_name'), data.get('dob'), data.get('gender'), 
            data.get('community'), data.get('student_mobile'), data.get('email'), 
            data.get('father_name'), data.get('parent_mobile'), data.get('address'), 
            data.get('district'), data.get('pincode'), data.get('mark10'), 
            data.get('per10'), data.get('mark12'), data.get('per12'), data.get('selected_course')
        ))
        conn.commit()
        conn.close()
        return jsonify({"status": "success", "message": "Application Submitted Successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)