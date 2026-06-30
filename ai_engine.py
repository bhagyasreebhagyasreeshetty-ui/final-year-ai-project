import google.generativeai as genai
import streamlit as st

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(prompt, language="English"):
    final_prompt = f"""
    Respond in {language}.

    {prompt}
    """

    response = model.generate_content(final_prompt)
    return response.text
