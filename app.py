import streamlit as st
import google.generativeai as genai

## Streamlit app layout
st.title('Personal Blog Writer')

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input fields for the product details
topic = st.text_area('Enter the Blog Topic:', placeholder='E.g., The Future of Artificial Intelligence')

# Button to generate blog content
if st.button('Generate Blog'):
    if topic.strip():  # Check if topic is not empty
        try:
            # Generate the blog using the API
            response = model.generate_content(prompt=topic, max_output_tokens=500)
            blog_content = response['text']  # Assuming API returns a 'text' key
            st.subheader('Generated Blog')
            st.write(blog_content)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning('Please enter a valid blog topic.')