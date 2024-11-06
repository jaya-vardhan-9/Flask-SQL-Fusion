from flask import Flask, request, send_file
import mysql.connector

app = Flask(__name__)

# Route to serve the index.html file at the root URL
@app.route('/', methods=['GET'])
def home():
    return send_file('index.html')

# Route to handle form submissions
@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from the form fields
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    age = request.form['age']
    street = request.form['street']
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip']
    gender = request.form['gender']
    comments = request.form['comments']
    subscribe = 'Yes' if 'subscribe' in request.form else 'No'

    # Establish a connection to the database
    connection = mysql.connector.connect(
        host='sql-server',  # Name of the SQL server container
        user='root',
        password='my-secret-pw',
        database='mydb'
    )
    cursor = connection.cursor()

    # Create table if not exists (optional)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100),
            last_name VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(15),
            age INT,
            street VARCHAR(255),
            city VARCHAR(100),
            state VARCHAR(100),
            zip_code VARCHAR(20),
            gender VARCHAR(20),
            comments TEXT,
            subscribe VARCHAR(10)
        )
    ''')

    # Insert data into the table
    cursor.execute('''
        INSERT INTO user_data (
            first_name, last_name, email, phone, age,
            street, city, state, zip_code, gender, comments, subscribe
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (first_name, last_name, email, phone, age, street, city, state, zip_code, gender, comments, subscribe))

    connection.commit()
    cursor.close()
    connection.close()

    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
