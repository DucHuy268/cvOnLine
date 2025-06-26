import streamlit as st


# Section Formation & Langue
def formation_section(langue="Français"):
    if langue == "Français":
        st.header("🎓 FORMATION")
        st.markdown("""
        - **Ingénierie des données** – [HEIA-FR](https://www.heia-fr.ch/) (2020 - 2023)  
        - **Computer Science** – [EPFL](https://www.epfl.ch/fr/) (2018)  
        - **Maturité fédérale – Option Mathématiques & Physique** – [Gymnase des Chamblandes](https://www.gymnasedechamblandes.ch/) (2015 - 2018)
        """)
    else:
        st.header("🎓 EDUCATION & LANGUAGES")
        st.markdown("""
        - **Data Engineering** – [HEIA-FR](https://www.heia-fr.ch/en/) (2020 - 2023)  
        - **Computer Science** – [EPFL](https://www.epfl.ch/en/) (2018)  
        - **Swiss High School Diploma – Math & Physics option** – [Gymnase des Chamblandes](https://www.gymnasedechamblandes.ch/) (2015 - 2018)
        """)

