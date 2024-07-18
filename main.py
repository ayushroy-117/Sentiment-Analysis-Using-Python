import nltk
from nltk.corpus import stopwords
from textblob import TextBlob

nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'

def main():
    filename = 'read.txt '  # Replace with your file name
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        preprocessed_line = preprocess_text(line)
        sentiment = analyze_sentiment(preprocessed_line)
        print(f"Original: {line.strip()}")
        print(f"Preprocessed: {preprocessed_line}")
        print(f"Sentiment: {sentiment}")
        print('-' * 40)

if __name__ == "__main__":
    main()
