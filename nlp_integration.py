import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
sid = SentimentIntensityAnalyzer()

def nltk_sentiment_analysis(text):
    sentiment_scores = []
    sentences = sent_tokenize(text)
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
        sentiment_score = sid.polarity_scores(' '.join(lemmatized_words))['compound']
        sentiment_scores.append(sentiment_score)
    avg_score = sum(sentiment_scores) / len(sentiment_scores)
    return avg_score

def textblob_keywords_extraction(text):
    blob = TextBlob(text)
    keywords = list(blob.noun_phrases)
    return keywords

def textblob_summarization(text):
    blob = TextBlob(text)
    summary = ' '.join([str(sentence) for sentence in blob.sentences[:3]])  # Extracting the first 3 sentences as a summary
    return summary


# Example usage
if __name__ == '__main__':
    sample_text = """
    Natural language processing (NLP) is a field focused on making sense of human language using computers.
    It involves tasks such as sentiment analysis, text summarization, machine translation, and more.
    NLTK and Gensim are popular libraries for NLP tasks in Python.
    """
    sentiment_score = nltk_sentiment_analysis(sample_text)
    keywords = textblob_keywords_extraction(sample_text)
    summary = textblob_summarization(sample_text)

    print("Sentiment Score:", sentiment_score)
    print("Keywords:", keywords)
    print("Summary:")
    print(summary)
