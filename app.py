import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="GeoHazards & GeoInformation Portfolio - Jhon Restrepo",
    page_icon="🌍",
    layout="wide"
)

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{encoded}"


# Set image as background
header_img = get_base64_image("images/Header.jpg")

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
st.markdown("---")

# Center-align image with vertical alignment using CSS
st.markdown("""
    <style>
    .centered-container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
    }
    .rounded-img {
        border-radius: 12px;
        max-width: 100%;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Create two columns
# About Me Section
st.subheader("About Me")

col1, col2 = st.columns([1, 2])  # Adjust ratio as needed

with col1:
    st.markdown("""
    <div class="centered-container">
        <img src="data:image/jpeg;base64,{}" class="rounded-img"/>
    </div>
    """.format(base64.b64encode(open("images/Me.jpg", "rb").read()).decode()), unsafe_allow_html=True)

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

📎 **LinkedIn**: [jhonrestrepogeologist](https://www.linkedin.com/in/jhonrestrepogeologist/)
""")
    
# --- Visualizations Section ---
st.markdown("---")
st.header("Visualizations")

# Section 1: Master Studies
st.subheader("1. Master Studies")

## First project - Earthquake analysis
st.markdown("**Analysis of earthquake coseismic displacement via InSAR and GNSS stations**")

col1, col2 = st.columns([1, 1])  # two equal columns

with col1:
    st.markdown("The map shows the epicentral location and seismic context.")

with col2:
    st.image("images/Pedernales_location.png", use_container_width=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("Derived interferogram with displacements calculated at the location of the selected GNSS stations.")

with col2:
    st.image("images/Pedernales_interferogram.png", use_container_width=True)


## Second project - Methane hotspots
st.markdown("**Showcasing Methane hotspots in northwestern South America**")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("Using 3-year average TROPOMI data, this analysis highlights Methane column concentrations along with wind speed in zones of Colombia and Venezuela.")

with col2:
    st.image("images/Methane.png", use_container_width=True)


# Section 2: Job Experience
st.subheader("2. Job Experience")

## Third job project - Deforestation
st.markdown("**Deforestation trends in two Pacific municipalities of Colombia**")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    Trends of deforestation analyzed from Hansen et al., (2013) with spatial focus on Riosucio and Rio Quito municipalities.

    This work resulted in a publication:  
    [Read the article here (In Spanish)](https://raccefyn.co/index.php/raccefyn/article/view/dinamicas_espacio_temporales_de_la_deforestacion_en_los_municipi)
    """)

with col2:
    st.image("images/Deforestation.jpg", use_container_width=True)


