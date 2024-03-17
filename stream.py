import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
sentiment = SentimentIntensityAnalyzer()
title = st.text_input("how do you feel about this hackathon?")


sent = sentiment.polarity_scores(title)
print(sent)