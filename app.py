import streamlit as st
from textblob import TextBlob

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
    st.subheader("Enter text for sentiment analysis:")

    user_input = st.text_area("Input text here:")
    
    if st.button("Analyze Sentiment"):
        if user_input:
            sentiment_result = analyze_sentiment(user_input)
            st.write(f"Sentiment: {sentiment_result}")
        else:
            st.warning("Please enter some text for analysis.")

if __name__ == "__main__":
    main()
