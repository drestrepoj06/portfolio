import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="GeoHazards & GeoInformation Portfolio - Jhon Restrepo",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
    <style>
    h1, h2, h3 {
        text-align: center;
    }
    p, div.stMarkdown > div > p {
        text-align: justify;
        text-justify: inter-word;
    }
    </style>
""", unsafe_allow_html=True)

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
st.markdown(
    '<h3 style="text-align: center;">Analysis of earthquake coseismic displacement via InSAR and GNSS positions</h3>',
    unsafe_allow_html=True,
)

st.markdown(
    '<p style="text-align: center;">Coseismic displacement in the near-field range of the 2016 Pedernales earthquake through position differences at four GNSS stations and a wrapped interferogram from Sentinel-1 imagery.</p>',
    unsafe_allow_html=True,
)

# Descriptions above images, side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("Epicentral location and seismic context.")

with col2:
    st.markdown("Derived interferogram with displacements calculated at the location of the selected GNSS stations.")

# Images side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.image("images/Pedernales_location.png", use_container_width=True)

with col2:
    st.image("images/Pedernales_interferogram.png", use_container_width=True)


## Second project - Methane hotspots
st.markdown(
    '<h3 style="text-align: center;">Showcasing Methane hotspots in northwestern South America</h3>',
    unsafe_allow_html=True,
)

# Additional description centered below the title
st.markdown(
    '<p style="text-align: center;">Using 3-year average (from 2019 to 2021) TROPOMI data, this analysis highlights Methane column concentrations along with wind speed in zones of Colombia and Venezuela.</p>',
    unsafe_allow_html=True,
)

# Descriptions above images, side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("Methane column above northwestern South America")

with col2:
    st.markdown("Emissions from wetlands in the area")

# Images side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.image("images/Methane.png", use_container_width=True)

with col2:
    st.image("images/Methane_wetland.png", use_container_width=True)


# Section 2: Job Experience
st.subheader("2. Job Experience")

## Third job project - Deforestation
st.markdown(
    '<h3 style="text-align: center;">Deforestation trends in two Pacific municipalities of Colombia</h3>',
    unsafe_allow_html=True,
)

# Centered text below title
st.markdown(
    """
    Spatial and temporal deforestation patterns in Riosucio and Río Quito municipalities in the Colombian Pacific region from 2015 to 2020 and to model a trend deforestation scenario for 2020-2025. The historical deforestation analysis (2015-2020) was done using the Global Forest Change database, while the future scenario (2020-2025) was modeled through Dinamica EGO.

    This work resulted in a publication:  
    [Read the article here (In Spanish)](https://raccefyn.co/index.php/raccefyn/article/view/dinamicas_espacio_temporales_de_la_deforestacion_en_los_municipi)
    """,
    unsafe_allow_html=True,
)

# Descriptions above images side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("Percentage of tree cover for the Pacific region with the Riosucio and Rio Quito municipalities.")
with col2:
    st.markdown("Simulated deforestation for 2025, along with validation percentage.")

# Images side by side
col1, col2 = st.columns([1, 1])

with col1:
    st.image("images/Deforestation_location.jpg", use_container_width=True)

with col2:
    st.image("images/Deforestation.jpg", use_container_width=True)




