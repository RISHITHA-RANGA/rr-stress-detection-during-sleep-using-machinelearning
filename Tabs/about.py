"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Name:
    Mainak Chaudhuri''')
    st.markdown('''### Email:
    mainakc24365@gmail.com''')
    st.image("./images/icon.jpg")
    st.markdown('''### GitHub: [Mainak](https://github.com/MainakRepositor/)''')
    