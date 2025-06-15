import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="GeoHazards & GeoInformation Portfolio - Jhon Restrepo",
    page_icon="🌍",
    layout="centered"
)

# Title and Date
st.title("GeoHazards & GeoInformation: Jhon Restrepo's Visualization Portfolio")
st.markdown("*Date: June 15, 2025*")

# Header line
st.markdown("---")

# About section
st.header("About Me")

# Create two columns
col1, col2 = st.columns([1, 3])  # Adjust ratio as needed (image:text)

with col1:
    st.image("images/Me.jpg", width=150)  # Adjust width to control image size

with col2:
    st.write("""
    A little bit about my education:  
    I am currently pursuing a Master in Geo-information Science and have completed a Bachelor in Geology.

    The following maps and figures below have been created throughout my job experience and studies.
    """)

# Separator
st.markdown("---")

# Maps section
st.header("Sample Maps")

st.image("images/Pedernales_location.png", caption="Pedernales Earthquake Location Map", use_container_width=True)
st.image("images/Pedernales_interferogram.png", caption="Pedernales Interferogram", use_container_width=True)
