import streamlit as st

from backend.services.recommendation_service import recommend_games

st.set_page_config(page_title="Game Recommendations", layout="wide")
st.title("🎲 Game Recommendations")

from ui.sidebar import render_sidebar

render_sidebar()

st.markdown(
    """
    Tell us a board game you enjoy, and we’ll recommend similar games you might like.
    """
)

game_name = st.text_input(
    "Enter a board game you like:",
    placeholder="e.g. Catan, Azul, Wingspan...",
)

if game_name:
    with st.spinner("Finding recommendations..."):
        recommendations = recommend_games(game_name)

    st.subheader("Recommended Games")
    st.markdown(recommendations)
