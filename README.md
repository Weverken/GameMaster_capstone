# GameMaster

The Ai-powered board game assistant

## Overview

GameMaster is a web-based application that helps board game players quickly understand rulebooks and discover new games they might enjoy.

During family board game nights, discussions often occur about the rules of the game. GameMaster allows users to upload a board game rulebook (PDF) and ask natural-language questions about the rules. The application extracts and structures the rules using a large language model, enabling accurate, conversational Q&A grounded in the original rulebook.

In addition, GameMaster provides a game recommendation feature and a small set of board-game utilities (dice roller, calculator, timer, and player order generator) to support gameplay.

## Features

- 📖 Rulebook Q&A
    - Upload a board game rulebook (PDF)
    - Automatically extract and structure rules
    - Ask natural-language questions with conversational memory
- 🎲 Game Recommendations
    - Enter a board game you like
    - Receive AI-generated recommendations for similar games
- 🧰 Game Utilities
    - Dice roller (d4–d20)
    - Simple calculator
    - Turn timer
    - Random player order generator

## Tech Stack

**Backend:**
- Python
- Google Gemini API (gemini-2.5-flash-lite)
- Pydantic (schema validation)
- Langfuse (observability & tracing)

**Frontend:**
- Streamlit

**AI/ML:**
- Google Gemini for rule extraction, Q&A, and recommendations
- Agent + tool-based architecture
- Structured schema extraction for rulebooks

## Architecture

GameMaster follows a clear separation of concerns between frontend and backend:

- **Frontend**
  - Streamlit pages
  - Shared sidebar UI component
  - Session state for chat history and UI state

- **Backend**
  - **Services**: rule extraction, Q&A logic, recommendations
  - **Agents**: route user intent and coordinate tool usage
  - **Tools**: focused, reusable functions (e.g., answering questions, summarizing rules)
  - **Utils**: configuration, prompt loading, observability setup

### Key Design Decisions
- Rule extraction is performed once and persisted to JSON to avoid repeated processing.
- Rulebook Q&A is stateful (with bounded conversation history).
- Game recommendations are stateless single-turn requests.
- Observability is integrated early to validate reasoning and detect issues.

## Installation & Setup

### Prerequisites
- Python 3.10+
- Google Gemini API key
- Langfuse account (optional but recommended)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/Weverken/GameMaster_capstone
cd GameMaster
```

2. Install dependencies:
```bash
uv sync
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

**Required environment variables:**
```
GOOGLE_API_KEY=your_gemini_api_key_here
LANGFUSE_PUBLIC_KEY=your_langfuse_public_key
LANGFUSE_SECRET_KEY=your_langfuse_secret_key
LANGFUSE_HOST=https://cloud.langfuse.com
```

4. Run the application:
```bash
uv run streamlit run app.py
```

## Usage

**Rulebook Q&A**
1. Navigate to Rulebook Q&A
2. Upload a board game rulebook PDF
3. Wait for extraction to complete
4. Ask questions about the rules in the chat interface
5. Use Clear Chat to reset the conversation without reprocessing the rulebook

**Game Recommendations**
1. Navigate to Game Recommendations
2. Enter the name of a board game you enjoy
3. View AI-generated recommendations

**Game Utilities**
1. Navigate to Game Utilities
2. Use the utilities as needed

## Deployment

**Live Application:** https://gamemaster-capstone.streamlit.app/

**Deployment Platform:** Streamlit Cloud

## Project Structure

```
GameMaster/
├── main.py                     # Home / landing page
├── pages/                      # Streamlit pages
│   ├── 1_Rulebook_QA.py
│   ├── 2_Game_Recommendations.py
│   └── 3_Game_Utilities.py
├── ui/
│   └── sidebar.py              # Shared sidebar component
├── backend/
│   ├── agents/                 # Agent orchestration logic
│   ├── services/               # Core business logic
│   ├── tools/                  # Tool functions used by agents
│   ├── schemas/                # Schemas for document parsing
│   └── utils/                  # Config, prompt loading, tracing
├── prompts/                    # System prompt text files
├── storage/                    # Uploaded PDFs & extracted rules
├── assets/
│   └── logo.png
├── docs/
│   └── architecture_plan.md    # Architectural reasoning
├── .env.example
├── requirements.txt
README.md
```

## Team

- Lowie De Wever
