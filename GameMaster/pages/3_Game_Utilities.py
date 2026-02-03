import streamlit as st
import random
import time

from ui.sidebar import render_sidebar

render_sidebar()

st.title("🧰 Game Utilities")
st.caption("Quick helpers for board game sessions")

st.divider()

# Four equal parts
col1, col2, col3, col4 = st.columns(4)

# Dice Roller
with col1:
    st.subheader("🎲 Dice Roller")

    dice = st.radio(
        "Choose dice",
        ["d4", "d6", "d8", "d10", "d12", "d20"],
        horizontal=True,
    )
    dice_size = int(dice[1:])

    if st.button("Roll Dice", use_container_width=True):
        st.success(f"🎲 Result: **{random.randint(1, dice_size)}**")


# Calculator
with col2:
    st.subheader("➕ Calculator")

    a = st.number_input("Number A", value=0, key="calc_a")
    b = st.number_input("Number B", value=0, key="calc_b")

    st.caption("Operation")

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    if c1.button("➕ Add", use_container_width=True):
        st.info(a + b)

    if c2.button("➖ Subtract", use_container_width=True):
        st.info(a - b)

    if c3.button("✖ Multiply", use_container_width=True):
        st.info(a * b)

    if c4.button("➗ Divide", use_container_width=True):
        if b == 0:
            st.error("Cannot divide by zero")
        else:
            st.info(a / b)


# Turn Timer
with col3:
    st.subheader("⏱ Turn Timer")

    seconds = st.slider(
        "Seconds per turn",
        min_value=10,
        max_value=300,
        value=60,
        step=10,
    )

    if st.button("Start Timer", use_container_width=True):
        with st.spinner("Timer running..."):
            time.sleep(seconds)
        st.success("⏰ Time's up!")


# Random Player Order
with col4:
    st.subheader("🎴 Player Order")

    players_text = st.text_area(
        "Players (one per line)",
        height=140,
        placeholder="Alice\nBob\nCharlie",
    )

    if st.button("Shuffle Order", use_container_width=True):
        players = [p.strip() for p in players_text.splitlines() if p.strip()]

        if len(players) < 2:
            st.warning("Enter at least two players")
        else:
            random.shuffle(players)
            for i, p in enumerate(players, start=1):
                st.write(f"{i}. {p}")
