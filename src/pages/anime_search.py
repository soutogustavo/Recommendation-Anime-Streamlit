import pandas as pd
import streamlit as st

@st.cache_data
def load_anime_data():
    """
    Load anima data
    """

    data_folder = "data"
    anime_data = pd.read_csv(f"{data_folder}/anime.csv")

    return anime_data

st.set_page_config(layout="wide")

#st.markdown("Anime Recommendation")
st.title("Anime Recommendation")

st.markdown("# :books: Search Anime")
st.sidebar.markdown("# Search :books:")

# Load anime data
anime_data = load_anime_data()

st.subheader("Search an anime")
text_search = st.text_input("Search anime by title", value="")
result_search = anime_data[anime_data["name"].str.contains(text_search)]

st.dataframe(
    result_search, 
    column_config={"anime_id": "Anime ID", 
                   "name": "Name", 
                   "genre": "Genre", 
                   "type": "Type", 
                   "episodes": "(Num) Episodes", 
                   "rating": "Rating",
                   "members": "(Num) Members"}, 
    use_container_width=True,
    hide_index=True)