import streamlit as st


# Section Compétences
def competences_section(langue="Français"):
    if langue == "Français":
        st.header("🧠 COMPÉTENCES")

        st.subheader("🤖 Intelligence Artificielle & Data")
        st.markdown("""
        - Machine Learning & Deep Learning  
        - Computer Vision & LLM  
        - Traitement de l'image & de texte  
        - Prompt Engineering, Data Mining
        """)

        st.subheader("💻 Développement")
        st.markdown("""
        - Python, Java, JavaScript, C++  
        - Vue.js & Node.js  
        - SQL, NoSQL, Spark, PL/SQL Oracle  
        - Spring, Spring Boot, RESTful APIs  
        - Linux (ligne de commande)
        """)

        st.subheader("☁️ DevOps & Cloud")
        st.markdown("""
        - Git, Docker, Kubernetes  
        - DevOps & MLOps, Micro-Services  
        - CI/CD
        """)
    else:
        st.header("🧠 SKILLS")

        st.subheader("🤖 Artificial Intelligence & Data")
        st.markdown("""
        - Machine Learning & Deep Learning  
        - Computer Vision & LLMs  
        - Image & Text Processing  
        - Prompt Engineering, Data Mining
        """)

        st.subheader("💻 Development")
        st.markdown("""
        - Python, Java, JavaScript, C++  
        - Vue.js & Node.js  
        - SQL, NoSQL, Spark, Oracle PL/SQL  
        - Spring, Spring Boot, RESTful APIs  
        - Linux (command line)
        """)

        st.subheader("☁️ DevOps & Cloud")
        st.markdown("""
        - Git, Docker, Kubernetes  
        - DevOps & MLOps, Microservices  
        - CI/CD pipelines
        """)
