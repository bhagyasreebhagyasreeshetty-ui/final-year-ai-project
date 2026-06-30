import streamlit as st
from ai_engine import ask_ai

st.title("AI Final Year Guide")

branch = st.selectbox("Select Branch", ["CSE", "ECE", "EEE", "MECH"])

domain = st.text_input("Enter Domain (AI, IoT, Cyber Security, Robotics)")

if st.button("Generate Complete Project"):
    prompt = f"""
You are a Final Year Project Expert.

Generate ONE unique industry-level project.

Branch: {branch}
Domain: {domain}

Provide:

1. Project Title
2. Problem Statement
3. Objective
4. Features
5. Tech Stack
6. System Architecture
7. Dataset Suggestions
8. Folder Structure
9. Database Design
10. API Design
11. Roadmap
12. Abstract
13. Literature Survey
14. Methodology
15. Expected Output
16. Future Scope
17. Viva Questions
18. Deployment Guide
19. Cost Estimation
20. Team Roles
"""

    language = st.session_state.get("language", "English")

    result = ask_ai(prompt, language)

    st.write(result)
