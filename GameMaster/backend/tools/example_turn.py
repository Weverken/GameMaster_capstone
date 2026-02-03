from backend.schemas.rules_schema import GameRules
from langfuse import observe

@observe()
def generate_example_turn(rules: GameRules) -> str:
    """
    Generates an example of what a typical turn looks like.
    """
    lines = [
        "**Example: Turn Walkthrough**",
        "",
        "A typical turn might proceed as follows:",
        "",
    ]

    for step in rules.round_structure:
        lines.append(f"- {step}")

    lines.extend([
        "",
        "This is a general example and may vary depending on player decisions.",
    ])

    return "\n".join(lines)
