from flask import Flask, request, jsonify
import os
import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

from openai import OpenAI

app = Flask(__name__)

def get_keyword_info(client, text):
    # Placeholder function for fetching definition information
    return f"Definition for '{text}'"

def summarize_text(client, text):
    # Placeholder function for text summarization
    return f"Summary of '{text}'"

def detect_sentiment_vader(text):
    # Placeholder function for sentiment analysis
    return "Positive" if "good" in text.lower() else "Negative"

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if not data or 'text' not in data or 'type' not in data:
        return jsonify({'error': 'Request must contain text and type fields'}), 400

    text = data['text']
    analysis_type = data['type'].lower()
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", "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"))

    if analysis_type == 'definition':
        result = get_keyword_info(client, text)
    elif analysis_type == 'summary':
        result = summarize_text(client, text)
    elif analysis_type == 'sentiment':
        result = detect_sentiment_vader(text)
    else:
        return jsonify({'error': 'Invalid analysis type. Choose from definition, summary, or sentiment'}), 400

    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)