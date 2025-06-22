import streamlit as st

# Section Langue
# def langues_section():
#     st.header("LANGUES")
#
#     st.markdown("""
#
#     | Langue       | Niveau                 | Détail                      |
#     |--------------|------------------------|-----------------------------|
#     | Vietnamien   | Langue maternelle      | Communication fluide        |
#     | Français     | C1 – Courant           | Utilisation quotidienne     |
#     | Anglais      | B2 – Professionnel     | Présentations et rédaction  |
#     """)

def langues_section(langue="Français"):
    if langue == "Français":
        st.header("🌐 LANGUES")

        st.markdown("""
        | Langue       | Niveau                 | Détail                      |
        |--------------|------------------------|-----------------------------|
        | Vietnamien   | Langue maternelle      | Communication fluide        |
        | Français     | C1 – Courant           | Utilisation quotidienne     |
        | Anglais      | B2 – Professionnel     | Présentations et rédaction  |
        """)
    else:
        st.header("🌐 LANGUAGES")

        st.markdown("""
        | Language     | Level                  | Detail                       |
        |--------------|------------------------|------------------------------|
        | Vietnamese   | Native language        | Fluent communication         |
        | French       | C1 – Fluent            | Daily professional usage     |
        | English      | B2 – Professional      | Presentations and writing    |
        """)
