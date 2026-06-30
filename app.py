import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Final Year Guide", layout="wide")

st.title("🎓 AI Final Year Guide")

st.write("Generate Final Year Projects using AI")

st.write("Use the pages menu on the left.")

domain = st.text_input(
    "Enter a domain",
    placeholder="Example: Artificial Intelligence",
)

if st.button("Generate Ideas"):
    prompt = f"""
    Give me 5 final year project ideas in {domain}.

    For each project provide:
    - Project Title
    - Description
    - Technologies Used
    - Difficulty
    """

    with st.spinner("Generating ideas..."):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

    st.markdown(response.text)
