from backend.schemas.rules_schema import GameRules
from backend.services.rules_qa import answer_rules_question as _answer
from langfuse import observe

@observe()
def answer_rules_question(rules: GameRules, question: str, chat_history: list[tuple[str, str]] = None) -> str:
    """
    Answers a specific question about the game rules.
    """
    return _answer(rules, question, chat_history)
