import pandas as pd
import streamlit as st

@st.cache_data
def load_recommendations_data():
    """
    Load recommendations data
    """

    data_folder = "data"
    filename = "recommendations_results.parquet"
    recommendations = pd.read_parquet(f"{data_folder}/{filename}")

    return recommendations

st.set_page_config(layout="wide")

st.title("Anime Recommendation")
st.markdown("# :movie_camera: Recommendation")
st.sidebar.markdown("# News :movie_camera:")

# Load recommendation data
recommendations_data = load_recommendations_data()

# Information
info_text = """
You can imagine this is streaming app, and each user gets 
(up to five) anime recommendations. Therefore, select a user
so that you can see the predicted recommendations.
"""
st.info(info_text, icon="ℹ️")

# Option: pick a user
option = st.selectbox(
    label='Select a user:',
    options=recommendations_data['user_id'].unique(),
    placeholder="Select used id...",
    index=None,)

# Select user recommendations
user_recommendations = recommendations_data[
    recommendations_data["user_id"] == option]

# Present results
st.write("You selected user: ", option)
st.dataframe(
    user_recommendations, 
    column_config={"user_id": st.column_config.NumberColumn(
                        "User ID",
                        format="%d",), 
                   "anime_id": st.column_config.NumberColumn(
                        "Anime ID",
                        format="%d",), 
                   "rating_est": st.column_config.NumberColumn(
                        "Rating (Est)",
                        help="Rating estimation",
                        format="%.2f ⭐",),
                   "name":"Name", 
                   "genre":"Genre", 
                   "type":"Type"}, 
    use_container_width=True,
    hide_index=True)