import streamlit as st


# Section Contact avec un formulaire interactif
def contact_section():
    st.header("Contact")
    st.markdown("""
    Pour toute question ou demande, merci de remplir le formulaire ci-dessous.
    """)
    with st.form("contact_form"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Envoyer")
        if submitted:
            st.success("Votre message a été envoyé. Merci !")

    st.markdown("""
    Vous pouvez aussi me joindre directement :  
    **Téléphone :** 078 854 13 68  
    **Email :** duchuy.nguyendasci@gmail.com
    """)
