import streamlit as st
from sections.accueil import accueil_section
from sections.competences import competences_section
from sections.experiences import experiences_section
from sections.formation import formation_section
from sections.header import header_section
from sections.langues import langues_section
from sections.like import like_section
from sections.projets import projets_section

langue = st.sidebar.selectbox("🌐 Language / Langue", ["Français", "English"])

if langue == "Français":
    st.sidebar.markdown("## 📌 Navigation")
    nav_selection = st.sidebar.radio("Aller à", [
        "🏠 Accueil",
        "🎓 Formation",
        "🌐 Langues",
        "🧠 Compétences",
        "💼 Expériences",
        "🛠️ Projets"
    ])
else:
    st.sidebar.markdown("## 📌 Navigation")
    nav_selection = st.sidebar.radio("Go to", [
        "🏠 Home",
        "🎓 Education",
        "🌐 Languages",
        "🧠 Skills",
        "💼 Work Experience",
        "🛠️ Projects"
    ])

# Affichage de l'en-tête commun en haut de la page
header_section()

# Gestion de la navigation via la barre latérale
if nav_selection == "🏠 Accueil" or nav_selection == "🏠 Home":
    accueil_section(langue)
elif nav_selection == "🎓 Formation" or nav_selection == "🎓 Education":
    formation_section(langue)
elif nav_selection == "🌐 Langues" or nav_selection == "🌐 Languages":
    langues_section(langue)
elif nav_selection == "🧠 Compétences" or nav_selection == "🧠 Skills":
    competences_section(langue)
elif nav_selection == "💼 Expériences" or nav_selection == "💼 Work Experience":
    experiences_section(langue)
elif nav_selection == "🛠️ Projets" or nav_selection == "🛠️ Projects":
    projets_section(langue)
# elif nav_selection == "✉️ Contact":
#     contact_section()

# Information supplémentaire dans la sidebar
st.sidebar.markdown("---")
if langue == "Français":
    st.sidebar.info("🚀 Ce CV interactif a été créé avec Streamlit\npar Duc Huy Nguyen – Data Engineer & Backend "
                    "Developer")

    with open("assets/DucHuyNguyen_CV.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Télécharger le CV",
            data=file,
            file_name="CV_DucHuyNguyen_Developer_IT.pdf",
            mime="application/pdf"
        )
else:
    st.sidebar.info("🚀 This interactive resume was built with Streamlit\nby Duc Huy Nguyen – Data Engineer & Backend "
                    "Developer")

    with open("assets/DucHuyNguyen_CV.pdf", "rb") as file:
        st.sidebar.download_button(
            label="📄 Download Resume",
            data=file,
            file_name="DucHuyNguyen_Resume_Developer_IT.pdf",
            mime="application/pdf"
        )


with st.sidebar:
    st.markdown("---")
    like_section(langue)

