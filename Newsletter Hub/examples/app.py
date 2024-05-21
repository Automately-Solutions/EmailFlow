from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

from rich.traceback import install
install(show_locals=True)

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

EMAIL_LIST_FILE = 'email_list.csv'

if not os.path.exists(EMAIL_LIST_FILE):
    df = pd.DataFrame(columns=['email'])
    df.to_csv(EMAIL_LIST_FILE, index=False)

@app.route('/add_email', methods=['POST'])
def add_email():
    data = request.json
    email = data.get('email')
    print(f"Request Data: {data}")  # Debug print
    if email:
        print(f"Received email: {email}")  # Debug print
        df = pd.read_csv(EMAIL_LIST_FILE)
        if email not in df['email'].values:
            print(f"Adding email: {email}")  # Debug print
            df = df.append({'email': email}, ignore_index=True)
            df.to_csv(EMAIL_LIST_FILE, index=False)
            print("Email added successfully")  # Debug print
            return jsonify({'message': 'Email added successfully!'}), 200
        else:
            print("Email already exists")  # Debug print
            return jsonify({'message': 'Email already exists!'}), 400
    print("Invalid email")  # Debug print
    return jsonify({'message': 'Invalid email!'}), 400

if __name__ == '__main__':
    app.run(debug=True)