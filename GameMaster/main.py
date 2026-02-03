import streamlit as st

from backend.utils.tracing import init_tracing

# Initialize tracing once
init_tracing()

from ui.sidebar import render_sidebar

render_sidebar()

# Page config MUST be first Streamlit call
st.set_page_config(
    page_title="GameMaster",
    page_icon="🎲",
    layout="wide",
)

# MAIN PAGE CONTENT

st.title("🎲 GameMaster")

st.markdown(
    """
    Welcome to **GameMaster**, whether you need help solving discussions during family game nights or want to find new games, GameMaster is the perfect companion.

    Use the sidebar to:
    - 📖 Upload a board game rulebook and ask questions about the rules  
    - 🎲 Discover new board games based on your favorites
    """
)

st.info("Select a page from the sidebar to get started.")

