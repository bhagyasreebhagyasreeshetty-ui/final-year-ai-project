import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def test_generate_content():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Hello"
    )

    assert response.text
    print(response.text)
