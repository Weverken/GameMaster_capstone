from pathlib import Path
import streamlit as st
import inspect


def render_sidebar():
    ASSETS_DIR = Path(__file__).parents[1] / "assets"

    # Hide default Streamlit page navigation
    st.markdown(
        """
        <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Detect current file
    current_file = Path(inspect.stack()[1].filename).name

    with st.sidebar:
        st.image(ASSETS_DIR / "logo.png", use_container_width=True)
        st.caption("Your AI-powered board game assistant")
        st.divider()

        # HOME
        is_home = current_file == "main.py"
        if st.button(
            "🏠 Home",
            use_container_width=True,
            type="primary" if is_home else "secondary",
        ):
            st.switch_page("main.py")

        st.divider()

        # RULEBOOK Q&A
        is_rules = current_file == "1_Rulebook_QA.py"
        if st.button(
            "📖 Rulebook Q&A",
            use_container_width=True,
            type="primary" if is_rules else "secondary",
        ):
            st.switch_page("pages/1_Rulebook_QA.py")

        # GAME RECOMMENDATIONS
        is_recs = current_file == "2_Game_Recommendations.py"
        if st.button(
            "🎲 Game Recommendations",
            use_container_width=True,
            type="primary" if is_recs else "secondary",
        ):
            st.switch_page("pages/2_Game_Recommendations.py")

        # GAME UTILITIES
        is_utils = current_file == "3_Game_Utilities.py"
        if st.button(
            "🧰 Game Utilities",
            use_container_width=True,
            type="primary" if is_utils else "secondary",
        ):
            st.switch_page("pages/3_Game_Utilities.py")
            
            # CLEAR CHAT
        if is_rules:
            st.divider()
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.chat_history = []
                st.rerun()
