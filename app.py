from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Game Hub", page_icon="🎮", layout="centered")

st.title("Game Hub")
mode = st.radio("Choose", ["Home", "Snake Game"], horizontal=True)

if mode == "Home":
    st.subheader("Games")
    st.markdown("- **Snake Game**: Play classic snake in browser")
    st.markdown("- **Roblox**: [Open Roblox](https://www.roblox.com)")
    st.info("Switch to 'Snake Game' above to play.")
else:
    snake_file = Path(__file__).with_name("snake.html")
    if not snake_file.exists():
        st.error("snake.html not found in project root.")
    else:
        html = snake_file.read_text(encoding="utf-8")
        components.html(html, height=760, scrolling=False)
