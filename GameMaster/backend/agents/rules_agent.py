from backend.schemas.rules_schema import GameRules
from backend.tools.summarize_rules import summarize_rules
from backend.tools.example_turn import generate_example_turn
from backend.tools.answer_questions import answer_rules_question

from langfuse import observe


class RulesAgent:
    """
    Agent responsible for routing rule-related user requests
    to the appropriate tool.
    """

    def classify_intent(self, user_input: str) -> str:
        text = user_input.lower()

        # Summarization
        summarize_keywords = [
            "summar",
            "overview",
            "brief",
            "explain the game",
            "what is this game",
            "how does this game work",
            "general idea",
        ]

        if any(k in text for k in summarize_keywords):
            return "summarize"

        # Example turn
        example_keywords = [
            "first turn",
            "example turn",
            "opening turn",
            "opening move",
            "how do i start",
            "what should i do in my turn",
            "initial turn",
        ]

        if any(k in text for k in example_keywords):
            return "example_turn"

        # Default: rules question
        return "question"
    
    @observe()
    def handle(
        self,
        rules,
        user_input: str,
        chat_history: list[tuple[str, str]],
    ) -> str:
        intent = self.classify_intent(user_input)

        if intent == "summarize":
            return summarize_rules(rules)

        if intent == "example_turn":
            return generate_example_turn(rules)

        return answer_rules_question(rules, user_input, chat_history)
