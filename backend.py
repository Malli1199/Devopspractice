from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) # Allows your HTML page to talk to this script safely

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    try:
        # 🔌 THIS IS HOW WE CONNECT TO MYSQL NATIVELY
        conn = mysql.connector.connect(
            host="127.0.0.1",       # Your local computer
            user="root",            # Your MySQL username
            password="root", # 👈 PUT YOUR ACTUAL MYSQL PASSWORD HERE
            database="devops_pipeline"
        )
        cursor = conn.cursor()
        
        # Create the table if you haven't already
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                username VARCHAR(50), 
                password VARCHAR(50)
            );
        """)
        
        # Insert the data sent from the HTML page
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": f"User {username} saved to MySQL!"}), 200
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Starts the local backend engine
    app.run(host='127.0.0.1', port=5000)