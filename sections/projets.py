import streamlit as st

# Section Projets / Études Spécifiques
def projets_section(langue="Français"):
    if langue == "Français":
        st.header("📂 ÉTUDES SPÉCIFIQUES")

        with st.expander("Travail de Bachelor - ArchiVision (HEIA-FR, Fribourg)"):
            st.markdown("""
            **Comment automatiser la description des façades de bâtiments à l'aide de modèles de deep learning (SAM,BLIP2, CLIP), tout en garantissant précision et adaptabilité face à la diversité architecturale ?**  
            Ce projet consistait à développer une application web permettant d'analyser automatiquement une photo de façade de bâtiment et d'en extraire des caractéristiques architecturales. L'application, développée avec Streamlit, fournit des informations telles que :
            - Le nombre de fenêtres  
            - Le nombre d'étages  
            - La présence d'un balcon  
            - Le ratio entre la surface des fenêtres et celle du bâtiment  

            Pour ce faire, des modèles de deep learning comme SAM, BLIP2 et CLIP ont été utilisés pour extraire ces informations à partir de l'image. L'application a été entièrement dockerisée pour garantir une portabilité et une mise en production simplifiée.  
            De plus, elle a été déployée sur un cluster Kubernetes, permettant une gestion scalable et une haute disponibilité.
            """)

        with st.expander("Projet du semestre 6 - Description des différences entre images/vidéos"):
            st.markdown("""
            **Période :** 03/2023 - 06/2023  
            Dans le contexte de la vidéosurveillance, nous souhaitons détecter et décrire instantanément par texte les objets présents dans la vidéo.  
            Cela permet d'économiser du temps pour la personne en charge de la surveillance, tout en évitant les fausses alertes.  
            Le modèle YOLOv8 est celui employé dans le cadre de ce projet.
            """)

        with st.expander("Projet du semestre 5 - Traitement de texte pour améliorer le modèle NLP"):
            st.markdown("""
            En appliquant des techniques de NLP pour extraire des mots-clés et des termes essentiels, nous avons enrichi le modèle.  
            Ce projet impliquait la classification de textes, et le défi majeur résidait dans l'extraction de mots-clés spécifiques à partir de textes variés, afin d'améliorer la capacité du modèle à effectuer une classification précise pour chaque texte distinct.
            """)

        with st.expander("Projet du semestre 4 - Système de recommandation pour films"):
            st.markdown("""
            Dans ce projet, nous avons dû concevoir un site web de films à l'image de Netflix, etc.  
            J'étais responsable de la partie backend, où j'ai mis en place un système de recommandation de films pour les utilisateurs en établissant une connexion avec le service RabbitMQ.  
            Pour le système de recommandation, j'ai employé la fonction de similarité cosinus pour suggérer des films susceptibles d'intéresser des profils similaires.
            """)

    else:
        st.header("📂 SPECIALIZED PROJECTS")

        with st.expander("Bachelor Thesis - ArchiVision (HEIA-FR, Fribourg)"):
            st.markdown("""
            **How can we automate the description of building facades using deep learning models (SAM, BLIP2, CLIP), while ensuring accuracy and adaptability across architectural diversity?**  
            This project consisted of developing a web application to automatically analyze a building facade photo and extract architectural features. Built using Streamlit, the app provides information such as:
            - Number of windows  
            - Number of floors  
            - Presence of a balcony  
            - Window-to-building surface ratio  

            To achieve this, deep learning models such as SAM, BLIP2, and CLIP were used to extract information from the image.  
            The app was fully dockerized for portability and simplified deployment, and deployed on a Kubernetes cluster for scalability and high availability.
            """)

        with st.expander("Semester 6 Project - Describing differences in images/videos"):
            st.markdown("""
            **Period:** 03/2023 - 06/2023  
            In the context of video surveillance, the goal was to instantly detect and describe objects in the scene using natural language.  
            This helps reduce operator workload and false alarms.  
            The model used was YOLOv8.
            """)

        with st.expander("Semester 5 Project - Text processing for NLP model improvement"):
            st.markdown("""
            We applied NLP techniques to extract keywords and essential terms to enrich the model.  
            The project involved text classification, and the main challenge was to extract domain-specific keywords from various documents to improve the model’s classification accuracy.
            """)

        with st.expander("Semester 4 Project - Movie recommendation system"):
            st.markdown("""
            This project involved designing a movie platform similar to Netflix.  
            I was in charge of the backend, where I implemented a recommendation system by integrating with RabbitMQ.  
            The cosine similarity function was used to suggest movies that matched user profiles.
            """)
