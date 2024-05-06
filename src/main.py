import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("Anime Recommendation")
st.markdown("# :star: Introduction")
st.sidebar.markdown("# Main page :star:")

introduction_txt = """
An Anime recommender system only on user viewing history.
In this Dashboard, you can...

- search for an anime
- get recommendations based on User (ID).

The recommendations were predicted using a technique called Collaborative Filtering.
"""

st.write(introduction_txt)