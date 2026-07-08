import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit page settings
st.set_page_config(
    page_title="AI Blog Generator",
    page_icon="✍️"
)

st.title("✍️ AI Blog Generator")
st.write("Generate a blog using Google Gemini AI")

# User input
topic = st.text_input("Enter your blog topic:")

length = st.selectbox(
    "Select blog length:",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Blog"):

    if topic:
        prompt = f"""
        Write a {length.lower()} blog on the topic:
        {topic}

        Include:
        - Title
        - Introduction
        - Main points
        - Conclusion
        """

        response = model.generate_content(prompt)

        st.subheader("Generated Blog")
        st.write(response.text)

    else:
        st.warning("Please enter a topic first.")
