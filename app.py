import streamlit as st
import sys

sys.path.append(".")

from src.recommender import recommend, movies
from src.tmdb import get_poster


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")

st.write("Find movies similar to the movie you like.")

selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:

        poster_url = get_poster(movie["id"])

        col1, col2 = st.columns([1, 2])

        with col1:
            if poster_url:
                st.image(poster_url, width=150)

        with col2:
            st.write(f"### 🎬 {movie['title']}")
            st.write(f"Similarity: {movie['score']}")