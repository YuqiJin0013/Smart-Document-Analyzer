from flask import Flask, request, jsonify
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from flask_cors import CORS
import logging
from fpdf import FPDF  # Import FPDF for PDF generation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})  # Enable CORS for frontend
logging.basicConfig(filename='backend_logs.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sid = SentimentIntensityAnalyzer()

from flask import request, send_from_directory

def analyze_sentiment(text):
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores['compound']

def text_summarization(text):
    sentences = sent_tokenize(text)
    return ' '.join(sentences[:3])  # Extract the first 3 sentences as a summary

def keyword_extraction(text):
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    return lemmatized_words

@app.route('/api/upload-file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    # Process and save the uploaded file
    # Example: file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return jsonify({'message': 'File uploaded successfully'}), 200

@app.route('/api/nlp/generate-document', methods=['POST'])
def generate_document():
    try:
        data = request.get_json()  # Parse JSON data from the request

        if 'text' not in data:
            return jsonify({'error': 'Text data is required'}), 400

        text = data['text']

        # Perform NLTK sentiment analysis on the text
        sentiment_score = analyze_sentiment(text)

        # Perform NLTK text summarization on the text
        summary = text_summarization(text)

        # Perform NLTK keyword extraction
        keywords = keyword_extraction(text)

        # Create PDF document using ReportLab
        pdf_path = "document_analysis.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawString(100, 750, "Document Analysis Results")
        c.drawString(100, 730, f"Sentiment Score: {sentiment_score}")
        c.drawString(100, 710, f"Summary: {summary}")
        c.drawString(100, 690, f"Keywords: {', '.join(keywords)}")
        c.save()
        
        # Add the document to the database (replace 'Your UID' with the actual user ID)
        # result = addDocument({'userID': 'Your UID', 'Text': text, 'Summary': summary, 'Sentiment': sentiment_score})

        return jsonify({'status': 'success', 'sentiment': sentiment_score, 'summary': summary, 'keywords': keywords, 'pdf_path': pdf_path}), 200
    except Exception as e:
        logging.error(f'Error processing NLP request: {e}')
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
