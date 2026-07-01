import os
from unittest.mock import MagicMock, patch

# Provide a dummy key string so client initialization doesn't throw a KeyError
os.environ.setdefault("GEMINI_API_KEY", "dummy_key")


@patch("google.genai.Client")
def test_generate_content(mock_client_class):
    # 1. Set up the mock structures to mirror the real SDK layout
    mock_client_instance = MagicMock()
    mock_client_class.return_value = mock_client_instance

    mock_response = MagicMock()
    mock_response.text = "Mocked AI response"
    mock_client_instance.models.generate_content.return_value = mock_response

    # 2. Act: Run the call logic using the mock client setup
    from google import genai

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Hello"
    )

    # 3. Assert: Verify the outputs match what we expect
    assert response.text == "Mocked AI response"
    mock_client_instance.models.generate_content.assert_called_once_with(
        model="gemini-2.5-flash", contents="Hello"
    )
