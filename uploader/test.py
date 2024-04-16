import requests

# Define the base URL for your Flask application
BASE_URL = 'http://localhost:5000'

def test_file_upload():
    # Path to the file you want to upload
    file_path = 'path/to/your/file.txt'

    # Open the file and prepare the data for upload
    with open(file_path, 'rb') as file:
        files = {'file': file}

        # Send a POST request to the upload endpoint
        response = requests.post(f'{BASE_URL}/upload', files=files)

        # Print the response
        print(response.json())

if __name__ == '__main__':
    test_file_upload()
