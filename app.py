import streamlit as st
import google.generativeai as genai

## Streamlit app layout
st.title('Personal Blog Writer')

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)