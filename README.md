This Python script utilizes the Natural Language Toolkit (nltk) and TextBlob libraries for text preprocessing and sentiment analysis. The script performs the following steps:

1. **Imports Necessary Libraries**: Imports nltk for stopword removal and TextBlob for sentiment analysis.
2. **Downloads Stopwords**: Ensures the necessary stopwords corpus is downloaded.
3. **Text Preprocessing Function**: Defines a function to remove stopwords from a given text and convert the remaining words to lowercase.
4. **Sentiment Analysis Function**: Defines a function to analyze the sentiment of the preprocessed text using TextBlob, categorizing it as either 'Positive' or 'Negative'.
5. **Main Function**: Reads lines from a specified text file, preprocesses each line, analyzes its sentiment, and prints the original, preprocessed text, and sentiment result.

To run the script, ensure you have a text file named 'read.txt' in the same directory. This script is useful for basic text preprocessing and sentiment analysis tasks.
