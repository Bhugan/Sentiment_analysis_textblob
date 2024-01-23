import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Sentiment Analysis App")
    
    # File uploader for CSV
    st.subheader("Upload a CSV file for sentiment analysis:")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        # Display the uploaded data
        st.subheader("Uploaded Data:")
        st.write(df)

        # Analyze sentiment for each row in the uploaded data
        df['Sentiment'] = df['Text'].apply(analyze_sentiment)

        # Display sentiment analysis results
        st.subheader("Sentiment Analysis Results:")
        st.write(df[['Text', 'Sentiment']])

        # EDA Section
        st.subheader("Exploratory Data Analysis (EDA):")
        
        # Bar chart for sentiment distribution
        plt.figure(figsize=(8, 6))
        sns.countplot(x='Sentiment', data=df)
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        st.pyplot(plt)

        # Display average sentiment score
        avg_sentiment = df['Sentiment'].value_counts(normalize=True).idxmax()
        st.write(f"Overall Sentiment: {avg_sentiment}")

if __name__ == "__main__":
    main()
