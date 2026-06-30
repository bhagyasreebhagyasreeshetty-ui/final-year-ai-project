import streamlit as st
from ai_engine import ask_ai

st.title("AI Project Assistant")

question = st.text_area("Ask Any Project Question")

if st.button("Ask AI"):
    language = st.session_state.get("language", "English")

    answer = ask_ai(question, language)

    st.write(answer)
