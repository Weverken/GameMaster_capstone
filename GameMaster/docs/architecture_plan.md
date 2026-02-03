# Team Project Architecture Plan

**Project Name:** GameMaster – Board Game Rulebook Assistant  

**Team Members:**
1. Lowie De Wever

**Project Domain:** ☐ Legal  ☐ Medical  ☐ Academic  ☐ Business  ☑ Other: Board Games / Entertainment

---

## Part 1: Project Overview

### What problem are you solving?

Modern board games often have complex rulebooks that are difficult to quickly reference during play. Players frequently need to pause the game to search for specific rules, which disrupts gameplay and reduces enjoyment.

---

### Who will use your application?

- Board game players
- Casual players learning a new game
- Groups that want quick rule clarification during gameplay

---

### What's your core value proposition? (In one sentence)

GameMaster allows players to instantly understand and query board game rules using natural language, without manually searching through rulebooks.

---

## Part 2: Define Your Layers

### UI Layer (Streamlit)

**What pages/screens do you need?**

1. **Main Page**
   - Purpose: Landing page and navigation hub for the application

2. **Rulebook Q&A Page**
   - Purpose: Upload a rulebook and ask conversational questions about the rules

3. **Game Recommendations Page**
   - Purpose: Recommend similar board games based on a user’s favorite game

4. **Game Utilities Page**
   - Purpose: Provide helpful board game tools (dice, calculator, timer, player order)

---

**User Inputs:**

- ☑ File upload (PDF)
  - File types: Board game rulebooks (PDF)
- ☑ Text input
  - For: Asking questions about rules, entering a favorite game name
- ☑ Dropdown / radio selections
  - For: Dice selection
- ☑ Sliders / numeric inputs
  - For: Turn timer duration, calculator inputs

---

**What do you display to users?**

- ☑ Extracted structured data (internal, used for grounding)
- ☑ Chat conversations
- ☐ Charts/visualizations
- ☐ Tables
- ☑ Other: Dice rolls, timers, player order lists

---

## Service Layer (Business Logic)

**Service 1:** Rule Extraction Service  
**Purpose:** Extract and structure board game rules from uploaded PDFs  

**Main responsibilities:**
- Extract raw text from PDF rulebooks
- Call Gemini to convert text into a structured schema
- Persist extracted rules to disk for reuse

---

**Service 2:** Rules Q&A Service  
**Purpose:** Answer user questions grounded in extracted rules  

**Main responsibilities:**
- Build prompts using structured rules and chat history
- Call Gemini to generate grounded answers
- Maintain bounded conversational context

---

**Service 3:** Recommendation Service  
**Purpose:** Recommend similar board games based on user input  

**Main responsibilities:**
- Accept a single game name as input
- Generate recommendations using Gemini
- Return results without storing conversational state

---

## Part 3: AI Layer (Gemini Operations)

**What AI operations do you need?**

- ☑ **Extract structured data from documents**
  - Extract fields such as setup steps, actions, scoring, and win conditions

- ☑ **Chat/Q&A with context**
  - About extracted board game rules

- ☑ **Summarization**
  - Summarize rules and provide example turns

- ☐ Classification/Categorization
- ☑ **Text generation**
  - Generate explanations and recommendations
- ☐ Comparison
- ☐ Analysis

---

**Will you need multi-turn conversations?**

☑ Yes  
☐ No  

**If yes, for what purpose:**  
To support follow-up questions when asking about rules.

---

## Tools Layer (Function Calling)

**Tool 1:** answer_questions
- Purpose: Generate an answer to a rules-related question
- Inputs: Structured rules, user question, recent chat history
- Output: Natural-language answer grounded in the rulebook

---

**Tool 2:** summarize_rules  
- Purpose: Produce a concise summary of a game’s rules
- Inputs: Structured rules
- Output: Short textual summary

---

**Tool 3:** example_turn 
- Purpose: Generate an example first turn for a board game
- Inputs: Structured rules
- Output: Step-by-step example turn

---

**Will AI call these automatically?**

☐ Yes, using function calling  
☑ No, services call them directly

---

## Part 4: Data Flow

**User Action:**  
User uploads a board game rulebook and asks a question about the rules.

**Step-by-Step Flow:**



```
1. User uploads PDF and asks a question
        ↓
2. Streamlit UI calls rule upload service
        ↓
3. Rule Extraction Service:
   a. Extracts text from PDF
   b. Sends text to Gemini
   c. Receives structured rules
        ↓
4. Rules Q&A Service called for answering questions
   Input: Structured rules + user question + chat history
   Output: Answer text
        ↓
5. (Optional) Tool functions used for summarization or examples
        ↓
6. Answer returned to UI
        ↓
7. User sees conversational response grounded in the rulebook
```

**Draw a diagram on paper/whiteboard showing this flow!**

---

## Part 5: Data Schema

### What structured data do you extract?

**Your Domain Schema:**

```json
{
  "field_name_1": "type and description",
  "field_name_2": "type and description",
  "field_name_3": ["list of what"],
  "nested_object": {
    "sub_field": "type"
  }
}
```

**Your Actual Schema:**

```json
{
  "game_title": "string",
  "player_count": "string",
  "play_time": "string",
  "age_rating": "string",
  "components": ["string"],
  "setup": ["string"],
  "objective": "string",
  "round_structure": ["string"],
  "actions": [
    {
      "name": "string",
      "description": "string"
    }
  ],
  "scoring": "string",
  "end_game": "string",
  "notes": ["string"]
}
```

**Required fields (must have):**
- game_title
- setup
- actions
- scoring
- end_game

**Optional fields (nice to have):**
- player_count
- play_time
- notes

---

## Part 5: Team Roles

**Who builds what:**

**Member 1:** Lowie De Wever → Responsible for: the whole app


---
