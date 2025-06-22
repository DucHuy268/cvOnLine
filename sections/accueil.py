import streamlit as st


# def accueil_section():
#     st.markdown("## 👤 Résumé / Profil")
#
#     st.markdown("**🧠 Qui suis-je ?**")
#     st.markdown(
#         "Je suis un ingénieur Data issu d'une formation spécialisée, mais mon profil va bien au-delà de ce titre. "
#         "Grâce à un parcours polyvalent, je me situe à l’intersection du développement logiciel, de l’ingénierie de la donnée et de la science des données. \n "
#         "\n Ma curiosité ne s’arrête pas aux frontières de la donnée : ce que je cherche avant tout, ce sont des défis IT stimulants — peu importe leur nature. "
#         "J’adore construire : des pipelines robustes, des modèles intelligents, des outils applicatifs ou encore des solutions backend sur mesure. "
#         "Je m'efforce toujours de poser une question simple mais puissante : « Et si les données pouvaient nous aider à résoudre ça ? » \n\n"
#         "À l’aise aussi bien avec des problématiques d’IA ou de performances, j’aborde chaque projet avec l’envie d’apprendre, d’itérer intelligemment, et d’ouvrir des perspectives concrètes grâce à la tech.")
#
#     st.markdown("**🤝 Quelle est ma valeur ajoutée en équipe ?**")
#     st.markdown(
#         "Je m’intègre vite, je communique clairement et je propose toujours des solutions concrètes. Je suis autonome, curieux, et j’ai cette volonté de créer un environnement technique fiable où chacun peut s’appuyer sur les fondations que je construis.")
#
#     st.markdown("**🔧 Quels sont mes outils de prédilection ?**")
#     st.markdown(
#         "Spring Boot, Python, PL/SQL, CI/CD, Kubernetes, modèles d’IA... Bref, ce qu’il faut pour bâtir une stack solide, durable, et scalable.")
#
#     st.markdown("**🌱 Quelle est ma philosophie professionnelle ?**")
#     st.markdown(
#         "Être proactif, apprendre en continu, ne pas avoir peur de remettre en question ce qui peut être amélioré, et faire équipe pour aller plus loin.")

def accueil_section(langue="Français"):
    if langue == "Français":
        st.markdown("## 👤 Résumé / Profil")

        st.markdown("**🧠 Qui suis-je ?**")
        st.markdown("""
        Je suis un ingénieur Data issu d'une formation spécialisée, mais mon profil va bien au-delà de ce titre.  
        Grâce à un parcours polyvalent, je me situe à l’intersection du développement logiciel, de l’ingénierie de la donnée et de la science des données.  

        Ma curiosité ne s’arrête pas aux frontières de la donnée : ce que je cherche avant tout, ce sont des défis IT stimulants — peu importe leur nature.  
        J’adore construire : des pipelines robustes, des modèles intelligents, des outils applicatifs ou encore des solutions backend sur mesure.  
        Je m'efforce toujours de poser une question simple mais puissante : « Et si les données pouvaient nous aider à résoudre ça ? »  

        À l’aise aussi bien avec des problématiques d’IA ou de performances, j’aborde chaque projet avec l’envie d’apprendre, d’itérer intelligemment, et d’ouvrir des perspectives concrètes grâce à la tech.
        """)

        st.markdown("**🤝 Quelle est ma valeur ajoutée en équipe ?**")
        st.markdown("Je m’intègre vite, je communique clairement et je propose toujours des solutions concrètes. Je suis autonome, curieux, et j’ai cette volonté de créer un environnement technique fiable où chacun peut s’appuyer sur les fondations que je construis.")

        st.markdown("**🔧 Quels sont mes outils de prédilection ?**")
        st.markdown("Spring Boot, Python, PL/SQL, CI/CD, Kubernetes, modèles d’IA... Bref, ce qu’il faut pour bâtir une stack solide, durable, et scalable.")

        st.markdown("**🌱 Quelle est ma philosophie professionnelle ?**")
        st.markdown("Être proactif, apprendre en continu, ne pas avoir peur de remettre en question ce qui peut être amélioré, et faire équipe pour aller plus loin.")

    else:
        st.markdown("## 👤 Summary / Profile")

        st.markdown("**🧠 Who am I?**")
        st.markdown("""
        I am a Data Engineer with a specialized academic background, but my profile goes far beyond that title.  
        Thanks to my multidisciplinary training, I operate at the crossroads of software development, data engineering, and data science.  

        My curiosity doesn’t stop at data: above all, I seek stimulating IT challenges — no matter the domain.  
        I love building things: robust pipelines, intelligent models, backend systems, or smart tooling.  
        I always strive to ask a simple but powerful question: “How can data help us solve this?”  

        Equally comfortable with AI, scalability or performance topics, I approach every project with a desire to learn, iterate efficiently, and unlock value through tech.
        """)

        st.markdown("**🤝 What do I bring to a team?**")
        st.markdown("I integrate quickly, communicate clearly, and always offer concrete solutions. I’m independent, curious, and committed to building technical foundations that others can rely on.")

        st.markdown("**🔧 My go-to technologies**")
        st.markdown("Spring Boot, Python, PL/SQL, CI/CD, Kubernetes, AI models... everything you need to build a reliable, scalable, future-ready stack.")

        st.markdown("**🌱 My professional philosophy**")
        st.markdown("Be proactive, keep learning, challenge what can be improved, and collaborate to go further.")
