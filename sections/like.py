import streamlit as st
import json
import os

LIKES_FILE = "likes.json"


def load_likes():
    if os.path.exists(LIKES_FILE):
        with open(LIKES_FILE, "r") as f:
            data = json.load(f)
            return data.get("likes", 0)
    return 0


def save_likes(count):
    with open(LIKES_FILE, "w") as f:
        json.dump({"likes": count}, f)


def like_section(langue="Français"):
    likes = load_likes()

    st.markdown("### ❤️ Vous aimez ce CV ?" if langue == "Français" else "### ❤️ Do you like this resume?")

    if st.button("👍 J’aime ce CV" if langue == "Français" else "👍 I like this resume"):
        likes += 1
        save_likes(likes)
        st.balloons()

    message = f"👍 {likes} personnes ont aimé ce CV." if langue == "Français" else f"👍 {likes} people liked this resume."
    st.markdown(message)
