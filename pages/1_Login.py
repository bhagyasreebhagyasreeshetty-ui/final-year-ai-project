import streamlit as st

st.title("User Login")

phone = st.text_input("Phone Number")
password = st.text_input("Password", type="password")

if st.button("Continue"):
    if phone and password:
        st.session_state["logged"] = True
        st.switch_page("pages/2_Language.py")
