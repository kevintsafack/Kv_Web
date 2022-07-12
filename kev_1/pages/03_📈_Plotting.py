import streamlit as st
import time
import numpy as np
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Plottingh Demo", page_icon="📈")



selected = option_menu(
        menu_title=None,
        options = ["Home","project","Contact"],
        icons = ["house","book","envelope"],
        orientation = "horizontal"
        
        )

if selected == "Home":
    st.title(f"you have selected {selected}")
    st.markdown("# Plotting Demo")
if selected == "project":
    st.title(f"you have selected {selected}")
    st.header("Plotting Demo")
if selected == "Contact":
    st.title(f"you have selected {selected}")
    st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)