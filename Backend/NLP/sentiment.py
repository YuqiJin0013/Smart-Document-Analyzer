from textblob import TextBlob

def detect_sentiment_textblob(text):
    """
    Detects the sentiment of the provided text using TextBlob.

    Parameters:
    - text (str): The text whose sentiment needs to be analyzed.

    Returns:
    - str: 'Positive', 'Negative', or 'Neutral' based on the sentiment analysis.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    # Classifying the sentiment based on the polarity score
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

'''import TextBlob from the textblob library for sentiment analysis.
The detect_sentiment_textblob function is defined to analyze the sentiment using TextBlob.

Inside the function, TextBlob(text) creates a TextBlob object for the given text, and blob.sentiment.
polarity calculates the polarity score (ranging from -1 (most negative) to 1 (most positive)) of the text.

The sentiment is classified based on the polarity score as 'Positive', 'Negative', or 'Neutral'.
Both NLTK's VADER and TextBlob are popular libraries for sentiment analysis in Python, with their own strengths and weaknesses. You can choose the one that best suits your requirements and accuracy expectations.'''