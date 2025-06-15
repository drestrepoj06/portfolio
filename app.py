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
""")
    
# --- Visualizations Section ---
st.markdown("---")
st.header("Visualizations")

# Section 1: Master Studies
st.subheader("1. Master Studies")

## First project - Epicentral map
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/Pedernales_location.png", use_container_width=True)
with col2:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Analysis of earthquake coseismic displacement via InSAR and GNSS stations</strong><br>
                The map shows the epicentral location and seismic context.
            </div>
        </div>
    """, unsafe_allow_html=True)

## Second project - Interferogram
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/Pedernales_interferogram.png", use_container_width=True)
with col2:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Analysis of earthquake coseismic displacement via InSAR and GNSS stations</strong><br>
                Derived interferogram with displacements calculated at the location of the selected GNSS stations.
            </div>
        </div>
    """, unsafe_allow_html=True)

## Third project - Methane hotspots
col1, col2 = st.columns([1.5, 1])
with col1:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Showcasing Methane hotspots in northwestern South America</strong><br>
                Using 3-year average TROPOMI data, this analysis highlights Methane column concentrations along with wind speed in zones of Colombia and Venezuela.
            </div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.image("images/Methane.png", use_container_width=True)

# Section 2: Job Experience
st.subheader("2. Job Experience")

## First job project - Deformation
col1, col2 = st.columns([1, 2])
# with col1:
    # st.image("images/sample1.png", use_container_width=True)
with col2:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Deformation in the North Pacific Seismogenic Zone, Colombia</strong><br>
                Analysis of focal mechanisms and velocity vectors to identify deformation patterns along the subduction interface.
            </div>
        </div>
    """, unsafe_allow_html=True)

## Second job project - Seismicity
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Seismicity for Tensor Inversion in Colombia</strong><br>
                Compilation of moment tensor solutions and focal mechanisms for regional tectonic interpretation.
            </div>
        </div>
    """, unsafe_allow_html=True)
# with col2:
    # st.image("images/sample2.png", use_container_width=True)

## Third job project - Deforestation
col1, col2 = st.columns([1, 2])
with col1:
    st.image("images/Deforestation.jpg", use_container_width=True)
with col2:
    st.markdown("""
        <div style="display: flex; align-items: center; height: 100%; min-height: 200px;">
            <div>
                <strong>Deforestation trends in two Pacific municipalities of Colombia</strong><br>
                Trends of deforestation analyzed from Hansen et al., (2013) with spatial focus on Riosucio and Rio Quito municipalities.
            </div>
        </div>
    """, unsafe_allow_html=True)



