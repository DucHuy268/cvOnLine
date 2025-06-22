import streamlit as st
from PIL import Image, ImageDraw


# Fonction d'affichage de l'en-tête (commune à toutes les sections)
def circle_crop_image(image_path, output_size=(200, 200)):
    # Ouvre l'image et convertit-la en mode RGBA pour gérer la transparence
    img = Image.open(image_path).convert("RGBA")
    # Redimensionne l'image
    img = img.resize(output_size, Image.LANCZOS)

    # Crée un masque circulaire
    mask = Image.new("L", output_size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse([(0, 0), output_size], fill=255)

    # Applique le masque à l'image pour obtenir une image circulaire
    img.putalpha(mask)
    return img

def header_section(langue="Français"):
    # Colonne image / infos
    col1, col2 = st.columns([1, 3])
    with col1:
        circular_img = circle_crop_image("assets/profile.jpeg")
        st.image(circular_img, use_container_width=False)
    with col2:
        st.title("Duc Huy Nguyen")
        st.subheader("Data Engineer / Backend Developer")

        if langue == "Français":
            st.markdown("""
            **📞 :** (+41) 078 854 13 68  
            **✉️ :** duchuy.nguyendasci@gmail.com  
            **📍 :** Rue du Léman 2, 1815 Clarens
            """)
        else:
            st.markdown("""
            **📞:** (+41) 078 854 13 68  
            **✉️:** duchuy.nguyendasci@gmail.com  
            **📍:** Rue du Léman 2, 1815 Clarens, Switzerland
            """)

    st.markdown("---")

