import streamlit as st


def like_section(langue="Français"):
    st.markdown("### ❤️ Vous aimez ce CV ?")

    if "likes" not in st.session_state:
        st.session_state.likes = 0

    if langue == "Français":
        if st.button("👍 J’aime ce CV"):
            st.session_state.likes += 1
        st.markdown(f"👍 {st.session_state.likes} personnes ont aimé ce CV.")
    else:
        if st.button("👍 I like this resume"):
            st.session_state.likes += 1
        st.markdown(f"👍 {st.session_state.likes} people liked this resume.")
