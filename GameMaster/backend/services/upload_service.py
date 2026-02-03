from pathlib import Path
import re

from backend.services.rules_extractor import (
    extract_pdf_text,
    extract_rules_structured,
    save_rules,
)

# Storage path resolution
PROJECT_ROOT = Path(__file__).resolve().parents[2]
STORAGE_DIR = PROJECT_ROOT / "storage"
UPLOADS_DIR = STORAGE_DIR / "uploads"
EXTRACTED_DIR = STORAGE_DIR / "extracted"


UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)

# Clean title for storage
def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_")


def process_uploaded_rulebook(pdf_bytes: bytes) -> dict:
    """
    Processes an uploaded rulebook PDF:
    - saves the PDF
    - extracts rules
    - saves structured rules
    - returns metadata and GameRules
    """
    # 1. Save temp file
    temp_pdf_path = UPLOADS_DIR / "temp_upload.pdf"
    temp_pdf_path.write_bytes(pdf_bytes)

    # 2. Extract rules
    text = extract_pdf_text(temp_pdf_path)
    rules = extract_rules_structured(text)

    # 3. Generate clean filenames
    game_slug = _slugify(rules.game_title or "unknown_game")

    pdf_path = UPLOADS_DIR / f"{game_slug}.pdf"
    json_filename = f"{game_slug}.json"

    # 4. Move & save
    temp_pdf_path.replace(pdf_path)
    save_rules(rules, json_filename)

    return {
        "rules": rules,
        "game_slug": game_slug,
        "pdf_path": pdf_path,
        "json_filename": json_filename,
    }
