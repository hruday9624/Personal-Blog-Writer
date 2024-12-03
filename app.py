import streamlit as st
import google.generativeai as genai

# Streamlit app layout
st.title('Personal Blog Writer with Prompt Engineering')

# Retrieve the API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets["GEMINI_API_KEY"]

# Configure the Google Generative AI API with your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Input field for the blog topic
topic = st.text_area('Enter the Blog Topic:', placeholder='E.g., The Future of Artificial Intelligence')

# Define a prompt template
prompt_template = (
    "Write a detailed blog about the topic: '{topic}'. "
    "Include an engaging introduction, key points with examples, and a thoughtful conclusion."
)

# Button to generate blog content
if st.button("Generate Blog"):
    if topic.strip():  # Ensure the topic is not empty
        try:
            # Generate the full prompt using the template
            full_prompt = prompt_template.format(topic=topic.strip())

            # Initialize the generative model
            model = genai.GenerativeModel("gemini-1.5-flash")  # Adjust the model as needed

            # Generate content based on the structured prompt
            response = model.generate_content(full_prompt)  # Pass the prompt

            # Check if a valid response is received
            if response and hasattr(response, 'text'):
                st.subheader("Generated Blog Content:")
                st.write(response.text)  # Display the generated text
            else:
                st.error("Error: Unable to generate blog content. Please try again.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid blog topic.")
