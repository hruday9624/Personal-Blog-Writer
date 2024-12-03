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
            # Initialize the generative model
            model = genai.GenerativeModel("gemini-1.5-flash")  # Adjust model name as needed
            # Generate the blog using the API
            response = model.generate_content(prompt=topic, max_output_tokens=500)
            
            # Extract and display the generated blog content
            blog_content = response.text
            st.subheader('Generated Blog')
            st.write(blog_content)
        except AttributeError:
            st.error("Failed to retrieve text from the response. Ensure the model is returning 'text'.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning('Please enter a valid blog topic.')
