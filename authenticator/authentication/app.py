from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Hardcoded username and password for demonstration purposes (replace with your actual authentication logic)
USERNAME = 'admin'
PASSWORD = 'password'

@app.route('/login', methods=['POST'])
def login():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return jsonify({'error': 'Authorization header is missing'}), 401

    auth_type, encoded_credentials = auth_header.split(' ')

    if auth_type.lower() != 'basic':
        return jsonify({'error': 'Only Basic authentication is supported'}), 401

    decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
    username, password = decoded_credentials.split(':')

    if username == USERNAME and password == PASSWORD:
        return jsonify({'message': 'Authentication successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)

'''
We import Flask, request, and jsonify from the Flask library, and base64 for encoding/decoding.
We define a route /login that accepts POST requests.
In the login function, we extract the Authorization header from the request and check if it's in the correct format (Basic authentication).
We decode the base64-encoded credentials and extract the username and password.
We compare the extracted username and password with hardcoded values (replace these with your actual authentication logic).
If the credentials match, we return a success message with status code 200. Otherwise, we return an error message with status code 401 (Unauthorized).
'''