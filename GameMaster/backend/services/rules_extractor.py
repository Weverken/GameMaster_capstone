from pathlib import Path

from backend.services.gemini_client import get_gemini_client
from backend.utils.settings import settings
from backend.schemas.rules_schema import GameRules
from backend.utils.prompts import PromptLoader 

from pypdf import PdfReader


# Path resolution
PROJECT_ROOT = Path(__file__).resolve().parents[2]

STORAGE_DIR = PROJECT_ROOT / "storage"
prompt_loader = PromptLoader()

# PDF to raw text

def extract_pdf_text(pdf_path: Path) -> str:
    """
    Extracts raw text from a PDF rulebook.
    """
    reader = PdfReader(pdf_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n".join(pages)



# Raw text to structured rules

def extract_rules_structured(rule_text: str) -> GameRules:
    """
    Uses Gemini to extract structured board game rules.
    """
    client = get_gemini_client()
    prompt = prompt_loader.load("extract_rules")

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=[
            prompt,
            "\n--- RULEBOOK TEXT ---\n",
            rule_text,
        ],
        config={
            "temperature": settings.GEMINI_TEMPERATURE,
            "response_mime_type": "application/json",
        },
    )

    return GameRules.model_validate_json(response.text)


# Save structured rules

def save_rules(
    rules: GameRules,
    filename: str,
) -> Path:
    """
    Saves extracted rules to GameMaster/storage/extracted/.
    Returns the full path to the saved file.
    """
    extracted_dir = STORAGE_DIR / "extracted"
    extracted_dir.mkdir(parents=True, exist_ok=True)

    output_path = extracted_dir / filename
    output_path.write_text(
        rules.model_dump_json(indent=2),
        encoding="utf-8",
    )

    return output_path

def load_rules(filename: str) -> GameRules:
    """
    Loads previously extracted rules from GameMaster/storage/extracted/.
    """
    extracted_dir = STORAGE_DIR / "extracted"
    path = extracted_dir / filename

    if not path.exists():
        raise FileNotFoundError(f"No extracted rules found at {path}")

    return GameRules.model_validate_json(
        path.read_text(encoding="utf-8")
    )


