import streamlit as st


# Section Expériences Professionnelles avec expandeurs pour plus d'interactivité
# def experiences_section():
#     st.header("EXPÉRIENCE PROFESSIONNELLE")
#
#     with st.expander("Utilisation des outils d’intelligence artificielle dans le développement"):
#         st.markdown("""
#         Je mobilise régulièrement des outils d’IA générative tels que **GitHub Copilot** et **ChatGPT** pour :
#
#         - 🔍 *Débugguer rapidement* du code complexe ou obscur
#         - 🧠 *Obtenir des suggestions* d’implémentation alternatives et plus robustes
#         - 🚀 *Optimiser les performances* de certains blocs critiques
#         - 💡 *Accélérer le prototypage* de fonctions ou structures algorithmiques
#         - 📚 *Rechercher de manière ciblée* des patterns ou bonnes pratiques de conception
#
#         Cette utilisation responsable et stratégique me permet de **gagner en productivité**,
#         de **renforcer la qualité du code livré**, et de **rester à jour** avec les meilleures pratiques du métier.
#         """)
#     with st.expander("Développeur Backend Java – Groupe Mutuel, Martigny"):
#         st.markdown("**Période :** 01.05.2024 - À ce jour")
#         st.markdown("**Référence :** Frédéric Aebi, Manager IT (Tel : 0848 803 111)")
#
#         st.markdown("### 🧾 Développement d’un module de facturation")
#         st.markdown("""
#         **Objectif :** Automatiser la génération de factures conformes aux spécifications métier.
#
#         - **Conception** du design de la facture selon les exigences fonctionnelles
#         - **Extraction** des données via Oracle SQL avec structuration par DTOs et Records
#         - **Transformation** en JSON via Java pour intégration dans un moteur de template
#         - **Transmission** du fichier JSON à une équipe externe en charge de la génération PDF
#         """)
#
#         st.markdown("### 🧱 Mise à jour et développement d’API Spring Boot")
#         st.markdown("""
#         **Objectif :** Renforcer la robustesse, la documentation et la scalabilité des API métier.
#
#         - Résolution d’un bug Swagger en migrant vers OpenAPI Specification
#         - Migration complète de MyBatis vers Spring Data JPA
#         - Développement de nouveaux modules backend performants
#         - Mise en place de tests (JUnit & Mockito) avec intégration continue via GitLab CI/CD
#         """)
#
#         st.markdown("### 🧩 Mise en place d’une convention de commit avec Regex")
#         st.markdown("""
#         **Objectif :** Améliorer la traçabilité des commits en standardisant les messages compatibles JIRA.
#
#         - Conception d’un pattern Regex imposé à tous les commits
#         - Intégration d’un contrôle dans GitLab pour valider le format avant merge
#         - Renforcement de la cohérence entre les développeurs et JIRA
#         """)
#
#     with st.expander("Migration des données de SQL Server – Flexdental, Epalinges"):
#         st.markdown("**Période :** 14.01.2024 - À ce jour")
#         st.markdown("**Référence :** Christelle Marclay, Directrice Générale (Tel : 0848 33 68 25)")
#
#         st.markdown("### 🎯 Objectif")
#         st.markdown(
#             "Assurer la transition des données radiologiques vers un nouveau logiciel tout en maintenant l'intégrité et la compatibilité des données.")
#
#         st.markdown("### 🛠️ Travaux réalisés")
#         st.markdown("""
#         - **Migration des images radiologiques :**
#           Supervision de la migration dans SQL Server, en gérant les différences de structures et de schémas entre les systèmes.
#
#         - **Automatisation avec Python :**
#           Développement de scripts ETL pour extraire, transformer et charger les données de manière fiable et répétable.
#
#         - **Adaptation et transformation :**
#           Restructuration des tables et ajustement des formats pour assurer la compatibilité avec la nouvelle solution logicielle.
#
#         - **Collaboration interdisciplinaire :**
#           Validation de l’intégrité des données avec un ingénieur pour garantir le bon fonctionnement du système après migration.
#         """)
#
#         st.markdown("### 👥 Intégration dans l’équipe")
#         st.markdown("""
#         - Adaptation rapide et collaboration fluide dès les premières semaines
#         - Développement autonome des solutions techniques
#         - Approche orientée qualité avec tests poussés avant mise en production
#         """)

def experiences_section(langue="Français"):
    if langue == "Français":
        st.header("💼 EXPÉRIENCE PROFESSIONNELLE")

        with st.expander("Utilisation des outils d’intelligence artificielle dans le développement"):
            st.markdown("""
            Je mobilise régulièrement des outils d’IA générative tels que **GitHub Copilot** et **ChatGPT** pour :

            - 🔍 *Débugguer rapidement* du code complexe ou obscur  
            - 🧠 *Obtenir des suggestions* d’implémentation alternatives et plus robustes  
            - 🚀 *Optimiser les performances* de certains blocs critiques  
            - 💡 *Accélérer le prototypage* de fonctions ou structures algorithmiques  
            - 📚 *Rechercher de manière ciblée* des patterns ou bonnes pratiques de conception

            Cette utilisation responsable et stratégique me permet de **gagner en productivité**,  
            de **renforcer la qualité du code livré**, et de **rester à jour** avec les meilleures pratiques du métier.
            """)

        with st.expander("Développeur Backend Java – Groupe Mutuel, Martigny"):
            st.markdown("**Période :** 01.05.2024 - À ce jour")
            st.markdown("**Référence :** Frédéric Aebi, Manager IT (Tel : 0848 803 111)")

            st.markdown("### 🧾 Développement d’un module de facturation")
            st.markdown("""
            **Objectif :** Automatiser la génération de factures conformes aux spécifications métier.

            - **Conception** du design de la facture selon les exigences fonctionnelles  
            - **Extraction** des données via Oracle SQL avec structuration par DTOs et Records  
            - **Transformation** en JSON via Java pour intégration dans un moteur de template  
            - **Transmission** du fichier JSON à une équipe externe en charge de la génération PDF
            """)

            st.markdown("### 🧱 Mise à jour et développement d’API Spring Boot")
            st.markdown("""
            **Objectif :** Renforcer la robustesse, la documentation et la scalabilité des API métier.

            - Résolution d’un bug Swagger en migrant vers OpenAPI Specification  
            - Migration complète de MyBatis vers Spring Data JPA  
            - Développement de nouveaux modules backend performants  
            - Mise en place de tests (JUnit & Mockito) avec intégration continue via GitLab CI/CD
            """)

            st.markdown("### 🧩 Mise en place d’une convention de commit avec Regex")
            st.markdown("""
            **Objectif :** Améliorer la traçabilité des commits en standardisant les messages compatibles JIRA.

            - Conception d’un pattern Regex imposé à tous les commits  
            - Intégration d’un contrôle dans GitLab pour valider le format avant merge  
            - Renforcement de la cohérence entre les développeurs et JIRA
            """)

        with st.expander("Migration des données de SQL Server – Flexdental, Epalinges"):
            st.markdown("**Période :** 14.01.2024 - À ce jour")
            st.markdown("**Référence :** Christelle Marclay, Directrice Générale (Tel : 0848 33 68 25)")

            st.markdown("### 🎯 Objectif")
            st.markdown(
                "Assurer la transition des données radiologiques vers un nouveau logiciel tout en maintenant l'intégrité et la compatibilité des données.")

            st.markdown("### 🛠️ Travaux réalisés")
            st.markdown("""
            - **Migration des images radiologiques :**  
              Supervision de la migration dans SQL Server, en gérant les différences de structures et de schémas entre les systèmes.

            - **Automatisation avec Python :**  
              Développement de scripts ETL pour extraire, transformer et charger les données de manière fiable et répétable.

            - **Adaptation et transformation :**  
              Restructuration des tables et ajustement des formats pour assurer la compatibilité avec la nouvelle solution logicielle.

            - **Collaboration interdisciplinaire :**  
              Validation de l’intégrité des données avec un ingénieur pour garantir le bon fonctionnement du système après migration.
            """)

            st.markdown("### 👥 Intégration dans l’équipe")
            st.markdown("""
            - Adaptation rapide et collaboration fluide dès les premières semaines  
            - Développement autonome des solutions techniques  
            - Approche orientée qualité avec tests poussés avant mise en production
            """)

    else:
        st.header("💼 WORK EXPERIENCE")

        with st.expander("Using artificial intelligence tools in development"):
            st.markdown("""
            I regularly use generative AI tools such as **GitHub Copilot** and **ChatGPT** to:

            - 🔍 *Quickly debug* complex or unclear code  
            - 🧠 *Get alternative, more robust implementation suggestions*  
            - 🚀 *Optimize performance* of critical code segments  
            - 💡 *Accelerate prototyping* of algorithms or technical structures  
            - 📚 *Search precisely* for design patterns and best practices

            This thoughtful and strategic use of AI helps me **increase productivity**,  
            **improve code quality**, and **stay aligned with modern development standards**.
            """)

        with st.expander("Backend Java Developer – Groupe Mutuel, Martigny"):
            st.markdown("**Period:** 01.05.2024 – Present")
            st.markdown("**Reference:** Frédéric Aebi, IT Manager (Tel: 0848 803 111)")

            st.markdown("### 🧾 Billing module development")
            st.markdown("""
            **Goal:** Automate invoice generation based on business specifications.

            - **Designed** invoice layout according to functional needs  
            - **Extracted** data via Oracle SQL using DTOs and Records  
            - **Transformed** into JSON using Java for integration with a template engine  
            - **Forwarded** the JSON to an external team in charge of PDF generation
            """)

            st.markdown("### 🧱 Updating and developing Spring Boot APIs")
            st.markdown("""
            **Goal:** Improve the robustness, documentation, and scalability of business APIs.

            - Fixed Swagger issue by migrating to OpenAPI Specification  
            - Fully migrated from MyBatis to Spring Data JPA  
            - Developed new high-performance backend modules  
            - Implemented unit tests (JUnit & Mockito) and CI/CD pipelines via GitLab
            """)

            st.markdown("### 🧩 Commit convention using Regex")
            st.markdown("""
            **Goal:** Improve commit traceability by standardizing message format for JIRA.

            - Designed a Regex pattern required for all commits  
            - Integrated a validation step in GitLab before merge  
            - Strengthened coherence across developers and JIRA tracking
            """)

        with st.expander("SQL Server data migration – Flexdental, Epalinges"):
            st.markdown("**Period:** 14.01.2024 – Present")
            st.markdown("**Reference:** Christelle Marclay, General Director (Tel: 0848 33 68 25)")

            st.markdown("### 🎯 Objective")
            st.markdown(
                "Ensure a smooth transition of radiology data to a new software system while maintaining data integrity and compatibility.")

            st.markdown("### 🛠️ Tasks performed")
            st.markdown("""
            - **Radiology image migration:**  
              Supervised migration in SQL Server, handling schema and structure mismatches between systems.

            - **Python automation:**  
              Developed ETL scripts for reliable and repeatable data migration.

            - **Restructuring and transformation:**  
              Adapted tables and formats to ensure compatibility with the new software solution.

            - **Cross-functional collaboration:**  
              Verified data integrity with an engineer to ensure post-migration system functionality.
            """)

            st.markdown("### 👥 Team integration")
            st.markdown("""
            - Rapid onboarding and smooth collaboration from the first weeks  
            - Autonomous development of technical solutions  
            - Quality-driven approach with thorough testing before deployment
            """)
