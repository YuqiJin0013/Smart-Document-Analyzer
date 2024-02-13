import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

def upload_file(request):
    # check if the post request has the file part
    if 'file' not in request.files:
        return {'error': 'No file part'}, 400

    file = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        return {'error': 'No selected file'}, 400

    # Check if the file has an allowed extension
    if '.' not in file.filename or \
       file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
        return {'error': 'Invalid file format'}, 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return {'message': 'File uploaded successfully', 'filename': filename}, 200

from textblob import TextBlob


def extract_paragraphs(document_text):
    # Split the document text into paragraphs
    paragraphs = document_text.split('\n\n')

    # Initialize a list to store analysis conclusions for each paragraph
    analysis_conclusions = []

    # Iterate over each paragraph
    for paragraph in paragraphs:
        # Perform text analysis on the paragraph
        blob = TextBlob(paragraph)
        sentiment_score = blob.sentiment.polarity

        # Determine the sentiment label based on the sentiment score
        if sentiment_score > 0:
            sentiment_label = 'positive'
        elif sentiment_score < 0:
            sentiment_label = 'negative'
        else:
            sentiment_label = 'neutral'

        # Add the analysis conclusion for the paragraph to the list
        analysis_conclusions.append({
            'paragraph': paragraph,
            'sentiment': sentiment_label
        })

    return analysis_conclusions



def deleteFile(userID, filePath):
    if userAuthentication(userID) == True:
        if delete_File(filePath):
            return 'deleted:' + filePath

def userAuthentication(userID):
    return True

def saveFile(filePath):
    return True

def delete_file(filePath):
    return True