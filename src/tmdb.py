import os
import requests
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

session = requests.Session()
session.headers.update({
    "User-Agent": "Movie-Recommendation-System/1.0"
})


def get_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": TMDB_API_KEY
    }

    response = session.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    poster_path = data.get("poster_path")

    if not poster_path:
        return None

    return f"https://image.tmdb.org/t/p/w500{poster_path}"