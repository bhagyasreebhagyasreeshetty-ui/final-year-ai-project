import streamlit as st

st.title("Select Language")

language = st.selectbox("Language", ["English", "Hindi", "Marathi", "Telugu"])

if st.button("Next"):
    st.session_state.language = language
    st.switch_page("pages/3_Dashboard.py")
