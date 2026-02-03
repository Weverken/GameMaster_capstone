from pathlib import Path
from langfuse import observe

from backend.services.gemini_client import get_gemini_client
from backend.utils.settings import settings
from backend.schemas.rules_schema import GameRules
from backend.utils.prompts import PromptLoader


# path resolution
PROJECT_ROOT = Path(__file__).resolve().parents[1]
prompt_loader = PromptLoader()

@observe()
def answer_rules_question(rules: GameRules, question: str, chat_history) -> str:
    """
    Answers a user question using extracted board game rules.
    """
    chat_history = chat_history or []
    client = get_gemini_client()
    rules_text = rules.model_dump_json(indent=2)

    history_text = "\n".join(
        f"{role}: {msg}" for role, msg in chat_history
    )
    prompt = prompt_loader.format(
    "rules_qa",
    rules_text=rules_text,
    chat_history=history_text,
    question=question,
)

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=[
            prompt,
            "\n--- RULES JSON ---\n",
            rules.model_dump_json(indent=2),
            "\n--- USER QUESTION ---\n",
            question,
        ],
        config={
            "temperature": 0.2,
        },
    )

    return response.text.strip()
