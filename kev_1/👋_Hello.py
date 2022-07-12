import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Hello",
    page_icon="📐",
)

st.write("# Welcome to Streamlit! 👋")

st.success("Select a demo above.")

st.markdown( # la markdown s'affiche en débu de page
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    try:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)
    except:
        st.write("Please enter an CSV file ")
    
    # To read file as bytes:
     #bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)

     # To convert to a string based IO:
     #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     #st.write(stringio)

     # To read file as string:
     #string_data = stringio.read()
     #st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
    