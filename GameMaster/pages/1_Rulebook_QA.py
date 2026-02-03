import streamlit as st

from backend.services.upload_service import process_uploaded_rulebook
from backend.services.rules_extractor import load_rules
from backend.agents.rules_agent import RulesAgent

st.set_page_config(page_title="Rulebook Q&A", layout="wide")
st.title("📖 Board Game Rulebook Q&A")

from ui.sidebar import render_sidebar

render_sidebar()


# Session state setup
if "rules_loaded" not in st.session_state:
    st.session_state.rules_loaded = False

if "rules" not in st.session_state:
    st.session_state.rules = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "rules_agent" not in st.session_state:
    st.session_state.rules_agent = RulesAgent()


# Upload section
st.header("Upload a Rulebook")

uploaded_file = st.file_uploader(
    "Upload a board game rulebook (PDF)",
    type=["pdf"],
)

if uploaded_file and not st.session_state.rules_loaded:
    with st.spinner("Extracting rules..."):
        result = process_uploaded_rulebook(uploaded_file.read())

        st.session_state.rules = result["rules"]
        st.session_state.rules_loaded = True
        st.session_state.game_slug = result["game_slug"]

    st.success(f"Rules for **{st.session_state.rules.game_title}** extracted!")

# Fallback load (cached rules)
if st.session_state.rules_loaded and st.session_state.rules is None:
    st.session_state.rules = load_rules("uploaded_game_rules.json")


# Chat section
if st.session_state.rules_loaded:
    st.header("Ask questions about the rules")

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)

    user_question = st.chat_input("Ask a question about the game rules")

    if user_question:
        st.session_state.chat_history.append(("user", user_question))

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = st.session_state.rules_agent.handle(
                    st.session_state.rules,
                    user_question,
                    st.session_state.chat_history,
                )
                st.write(answer)

        st.session_state.chat_history.append(("assistant", answer))
