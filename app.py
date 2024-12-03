import streamlit as st
import google.generativeai as genai

# Streamlit app layout
st.title('Personal Blog Writer')

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input field for the blog topic
topic = st.text_area('Enter the Blog Topic:', placeholder='E.g., The Future of Artificial Intelligence')

# Button to generate blog content
if st.button('Generate Blog'):
    if topic.strip():  # Check if topic is not empty
        try:
            # Generate the blog using the API
            response = genai.generate_text(
                prompt=topic,
                max_output_tokens=500
            )
            blog_content = response['candidates'][0]['output']  # Extract text from the response
            st.subheader('Generated Blog')
            st.write(blog_content)
        except KeyError:
            st.error("Failed to retrieve generated text from the response.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning('Please enter a valid blog topic.')
