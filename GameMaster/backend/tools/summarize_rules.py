from backend.schemas.rules_schema import GameRules
from langfuse import observe

@observe()
def summarize_rules(rules: GameRules) -> str:
    """
    Generates a concise summary of the game's rules.
    """
    lines = [
        f"**Objective**: {rules.objective}",
        "",
        f"**Players**: {rules.player_count or 'Not specified'}",
        "",
        "**Core Actions:**",
    ]

    for action in rules.actions[:5]:
        lines.append(f"- **{action.name}**: {action.description}")

    lines.extend([
        "",
        f"**End Game**: {rules.end_game}",
    ])

    return "\n".join(lines)
