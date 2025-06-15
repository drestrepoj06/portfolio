import streamlit as st
from datetime import datetime

# Page config (optional)
st.set_page_config(
    page_title="GeoHazards & GeoInformation Portfolio - Jhon Restrepo",
    page_icon="🌍",
    layout="centered"
)

# Title and Date
st.title("GeoHazards & GeoInformation: Jhon Restrepo's Visualization Portfolio")
st.markdown(f"*Date: June 15, 2025*")

# Nice header line
st.markdown("---")

# About section
st.header("About Me")
st.image("images/Me.jpg", caption="Pedernales Earthquake Location Map", use_container_width=False)
st.write("""
A little bit about my education:  
I am currently pursuing a Master in Geo-information Science and have completed a Bachelor in Geology.

The following maps and figures below have been created throughout my job experience and studies.
""")


# Another separator
st.markdown("---")

# Display images with captions
st.header("Sample Maps")

st.image("images/Pedernales_location.png", caption="Pedernales Earthquake Location Map", use_container_width=True)
st.image("images/Pedernales_interferogram.png", caption="Pedernales Interferogram", use_container_width=True)
