from pathlib import Path

from langfuse import observe

from backend.services.gemini_client import get_gemini_client
from backend.utils.settings import settings
from backend.utils.prompts import PromptLoader


PROJECT_ROOT = Path(__file__).resolve().parents[1]
prompt_loader = PromptLoader()

@observe()
def recommend_games(game_name: str) -> str:
    """
    Recommends board games similar to the given game.
    """
    client = get_gemini_client()
    prompt = prompt_loader.format(
    "game_recommendations",
    game_name=game_name,
    )

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=[
            prompt,
            "\n--- USER INPUT ---\n",
            game_name,
        ],
        config={
            "temperature": 0.5,
        },
    )

    return response.text.strip()