import ast
from pathlib import Path
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# 1. Load datasets
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

movies = pd.read_csv(BASE_DIR / "data" / "tmdb_5000_movies.csv")
credits = pd.read_csv(BASE_DIR / "data" / "tmdb_5000_credits.csv")


# -----------------------------
# 2. Helper functions
# -----------------------------

def convert_names(text):
    items = ast.literal_eval(text)

    names = []

    for item in items:
        names.append(item["name"])

    return " ".join(names)


def convert_cast(text):
    cast_list = ast.literal_eval(text)

    names = []

    for actor in cast_list[:3]:
        names.append(actor["name"])

    return " ".join(names)


def get_director(text):
    crew_list = ast.literal_eval(text)

    for person in crew_list:
        if person["job"] == "Director":
            return person["name"]

    return ""


# -----------------------------
# 3. Clean data
# -----------------------------

movies["genres"] = movies["genres"].apply(convert_names)
movies["keywords"] = movies["keywords"].apply(convert_names)

movies["cast"] = credits["cast"].apply(convert_cast)
movies["director"] = credits["crew"].apply(get_director)

movies["overview"] = movies["overview"].fillna("")


# -----------------------------
# 4. Keep required columns
# -----------------------------

movies = movies[
    ["id", "title", "genres", "keywords", "overview", "cast", "director"]
]


# -----------------------------
# 5. Create tags
# -----------------------------

movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"] + " " +
    movies["cast"] + " " +
    movies["director"]
)

movies["tags"] = movies["tags"].str.lower()


# -----------------------------
# 6. TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer(max_features=5000)

vectors = vectorizer.fit_transform(movies["tags"])


# -----------------------------
# 7. Cosine similarity
# -----------------------------

similarity = cosine_similarity(vectors)


# -----------------------------
# 8. Movie title lookup
# -----------------------------

movie_indices = pd.Series(
    movies.index,
    index=movies["title"]
).drop_duplicates()


# -----------------------------
# 9. Recommendation function
# -----------------------------

def recommend(movie):

    movie = movie.lower()

    title_map = {
        title.lower(): title
        for title in movies["title"]
    }

    if movie not in title_map:
        return []

    actual_title = title_map[movie]

    index = movie_indices[actual_title]

    similar_movies = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i in similar_movies[1:6]:

        recommendations.append({
            "id": int(movies.iloc[i[0]]["id"]),
            "title": movies.iloc[i[0]]["title"],
            "score": float(round(i[1], 3))
        })

    return recommendations