import unittest
import base64
from app import app  # Import the Flask app from app.py

# Helper function to encode username and password for Basic authentication
def encode_credentials(username, password):
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    return f"Basic {encoded_credentials}"

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()

    def test_successful_authentication(self):
        # Encode credentials for authentication
        auth_header = encode_credentials('admin', 'password')
        headers = {'Authorization': auth_header}

        # Send a POST request to the login endpoint
        response = self.app.post('/login', headers=headers)

        # Assert that the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Assert that the response JSON contains a success message
        self.assertIn(b'Authentication successful', response.data)

    def test_invalid_credentials(self):
        # Encode invalid credentials for authentication
        auth_header = encode_credentials('invalid_user', 'invalid_password')
        headers = {'Authorization': auth_header}

        # Send a POST request to the login endpoint with invalid credentials
        response = self.app.post('/login', headers=headers)

        # Assert that the response status code is 401 (unauthorized)
        self.assertEqual(response.status_code, 401)

        # Assert that the response JSON contains an error message
        self.assertIn(b'Invalid credentials', response.data)

if __name__ == '__main__':
    unittest.main()


'''
We import unittest for writing unit tests.
The encode_credentials function is a helper function that takes a username and password, encodes them using base64, and formats them as a Basic authentication header.
We create a test case class AuthenticationTestCase that inherits from unittest.TestCase.
In the setUp method, we create a test client for the Flask app using app.test_client().
We define two test methods: test_successful_authentication and test_invalid_credentials.
Inside each test method, we encode credentials, set them in the request headers, and send a POST request to the /login endpoint using the test client.
We use assertions to check the expected behavior, such as verifying the response status code and response message.

To run the unit tests, you can execute the unit_test.py file. 
It will automatically discover and run the test cases defined in the test case class. If all tests pass, you should see output indicating that all tests were successful.
'''