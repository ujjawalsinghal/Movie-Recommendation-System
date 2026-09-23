import streamlit as st
import sys

sys.path.append(".")

from src.recommender import recommend, movies


# Page configuration
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬"
)

# Title
st.title("🎬 Movie Recommendation System")
st.write("Find movies similar to the movie you like.")


# Movie selection
selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)


# Recommendation button
if st.button("Recommend"):
    
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(
            f"🎬 **{movie['title']}** — "
            f"Similarity: {movie['score']}"
        )