"""
Prompt management utilities.
Load and format prompts from text files.
"""

from pathlib import Path


class PromptLoader:
    """Load and manage prompt templates from files."""

    def __init__(self, prompts_dir: Path | None = None):
        """
        Initialize prompt loader.

        Args:
            prompts_dir: Path to prompts directory (defaults to project_root/prompts)
        """
        if prompts_dir is None:
            # backend/utils/prompt_loader.py -> backend/utils -> backend -> project root
            project_root = Path(__file__).resolve().parents[2]
            prompts_dir = project_root / "prompts"

        self.prompts_dir = Path(prompts_dir)

    def load(self, prompt_name: str) -> str:
        """
        Load a prompt template from file.

        Args:
            prompt_name: Name of prompt file (without .txt)

        Returns:
            Prompt template string
        """
        prompt_path = self.prompts_dir / f"{prompt_name}.txt"

        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

        return prompt_path.read_text(encoding="utf-8")

    def format(self, prompt_name: str, **kwargs) -> str:
        """
        Load and format a prompt template with variables.
        """
        template = self.load(prompt_name)
        return template.format(**kwargs)
