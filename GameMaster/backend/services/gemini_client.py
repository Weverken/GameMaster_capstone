from google import genai
from backend.utils.settings import settings

_client: genai.Client | None = None


def get_gemini_client() -> genai.Client:
    """
    Returns a singleton Gemini client.
    """
    global _client

    if _client is None:
        _client = genai.Client(api_key=settings.GEMINI_API_KEY)

    return _client
