import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Set up NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def analyze_text(text):
    # Tokenize text
    tokens = word_tokenize(text)

    # Remove punctuation and stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]

    # Calculate word frequency
    freq_dist = FreqDist(tokens)

    # Get the most common words
    most_common_words = freq_dist.most_common(10)

    return {'most_common_words': most_common_words}
