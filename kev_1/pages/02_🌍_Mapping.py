import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_option_menu import option_menu
#from 01_📊_DataFrame import P
st.set_page_config(page_title="Mapping Demo", page_icon="🌍")


selected = option_menu(
        menu_title=None,
        options = ["Home","project","Contact"],
        icons = ["house","book","envelope"],
        orientation = "horizontal"
        
        )

if selected == "Home":
    st.title(f"you have selected {selected}")
    st.markdown("# Mapping Demo")
if selected == "project":
    st.title(f"you have selected {selected}")
    st.header("Mapping Demo")
if selected == "Contact":
    st.title(f"you have selected {selected}")
    st.write(
        """This demo shows how to use
    [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
    to display geospatial data."""
    )
    


