import streamlit as st

st.title("Dashboard")

st.write("Selected Language:", st.session_state.get("language"))

st.page_link("pages/4_Project_Generator.py", label="Open Project Generator")
