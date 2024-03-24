from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from text_analysis import analyze_text

app = Flask(__name__)

# Set up folder for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}  # Add more if needed
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Secure file uploader endpoint
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})
    else:
        return jsonify({'error': 'File type not allowed'})

# Text NLP analysis endpoint
@app.route('/analyze', methods=['POST'])
def analyze_endpoint():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'})

    text = data['text']
    result = analyze_text(text)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
