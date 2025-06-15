import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="GeoHazards & GeoInformation Portfolio - Jhon Restrepo",
    page_icon="🌍",
    layout="centered"
)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{encoded}"

header_img = get_base64_image("images/Header.jpg")

# Custom header with background image
st.markdown(
    f"""
    <div style="
        background-image: url('{header_img}');
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        border-radius: 10px;
        text-align: center;
        color: white;
    ">
        <h1>GeoHazards & GeoInformation:<br>Jhon Restrepo's Visualization Portfolio</h1>
        <p><em>Date: June 16, 2025</em></p>
    </div>
    """,
    unsafe_allow_html=True
)

# Header line
st.markdown("---")

# About section
st.header("About Me")

# Create two columns
col1, col2 = st.columns([1, 3])  # Adjust ratio as needed (image:text)

with col1:
    st.image("images/Me.jpg", width=150)  # Adjust width to control image size

with col2:
    st.markdown("""
**My education:**  
- Master in Geo-information Science with focus on Remote Sensing  
- Bachelor in Geology  

**My job experience:**  
- AI trainer for programming Large Language Models at Outlier.ai  
- Physics and math tutor at tutor.com  
- GNSS and seismology data analyst at Colombian Geological Survey  
- Physics and math tutor at Universidad del Norte  

The following maps and figures below have been created throughout my job experience and studies.
""")

# Separator
st.markdown("---")

# Maps section
st.header("Sample Maps")

st.image("images/Pedernales_location.png", caption="Pedernales Earthquake Location Map", use_container_width=True)
st.image("images/Pedernales_interferogram.png", caption="Pedernales Interferogram", use_container_width=True)
