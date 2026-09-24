# 🎬 Movie Recommendation System

A content-based movie recommendation system built using Python, Pandas, Scikit-learn, NLP techniques, and Streamlit.

The system recommends movies similar to a movie selected by the user. It analyzes movie information such as genres, keywords, overview, cast, and director, converts this information into numerical representations using TF-IDF, and calculates similarity between movies using cosine similarity.

The application also integrates the TMDB API to retrieve and display movie posters for the recommended movies.

## ✨ Features

- 🎬 Recommends movies similar to a selected movie
- 🔍 Case-insensitive movie title search
- 🧠 Content-based recommendation using TF-IDF
- 📐 Cosine similarity for measuring movie similarity
- 🎭 Uses genres, keywords, overview, cast, and director
- 🖼️ Fetches movie posters using the TMDB API
- 🌐 Interactive Streamlit web interface
- 📊 Displays similarity scores for recommendations

## 🧠 How It Works

The recommendation system follows a content-based filtering approach.

### 1. Data Collection

The project uses the TMDB 5000 Movie Dataset, which contains movie information such as:

- Movie title
- Genres
- Keywords
- Overview
- Cast
- Crew

### 2. Data Preprocessing

The genres, keywords, cast, and crew information is stored as structured text. These fields are processed to extract useful information.

For each movie:

- Genres are extracted
- Keywords are extracted
- The first three cast members are selected
- The director is extracted from the crew information
- Missing movie overviews are handled

### 3. Feature Engineering

The extracted information is combined into a single `tags` column containing:

- Genres
- Keywords
- Overview
- Cast
- Director

The tags are converted to lowercase before vectorization.

### 4. TF-IDF Vectorization

The `tags` column is converted into numerical vectors using `TfidfVectorizer` from Scikit-learn.

The vectorizer is configured with a maximum of 5,000 features.

### 5. Cosine Similarity

Cosine similarity is calculated between the TF-IDF vectors of all movies.

Movies with more similar content receive higher similarity scores.

### 6. Recommendation

When the user selects a movie:

1. The selected movie is located in the dataset.
2. Its similarity scores are retrieved.
3. Movies are sorted by similarity.
4. The selected movie itself is excluded.
5. The top five similar movies are returned.

### 7. TMDB Poster Integration

Each recommendation contains its TMDB movie ID.

The application sends this ID to the TMDB API to retrieve the movie's poster path. The poster is then displayed in the Streamlit interface.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | TF-IDF vectorization and cosine similarity |
| Matplotlib | Data visualization |
| Seaborn | Data visualization |
| Jupyter Notebook | Data exploration and development |
| Streamlit | Web application interface |
| Requests | TMDB API requests |
| python-dotenv | Securely loading the TMDB API key |
| TMDB API | Movie poster retrieval |
| Git & GitHub | Version control and project hosting |

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── docs/
│   └── Movie_Recommendation_System_Project_Documentation.docx
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── src/
│   ├── recommender.py
│   └── tmdb.py
│
└── venv/
```

## 📊 Dataset

This project uses the **TMDB 5000 Movie Dataset**.

The dataset consists of two files:

- `tmdb_5000_movies.csv` — contains movie information such as title, genres, keywords, overview, and TMDB movie ID.
- `tmdb_5000_credits.csv` — contains cast and crew information.

The dataset contains **4,803 movies**.

### Features Used

The recommendation system uses the following information:

- Movie title
- Genres
- Keywords
- Overview
- Top three cast members
- Director

These features are combined into a single `tags` representation for the recommendation algorithm.

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ujjawalsinghal/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the TMDB API Key

Create a `.env` file in the project root:

```env
TMDB_API_KEY=YOUR_TMDB_API_KEY
```

Replace `YOUR_TMDB_API_KEY` with your own TMDB API key.

**Do not commit the `.env` file to GitHub.**

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address.

## 🎞️ TMDB API Integration

The application uses the TMDB API to retrieve poster information for recommended movies.

The recommendation engine stores the TMDB movie ID for each recommendation. This ID is passed to the TMDB API, which returns the corresponding movie information and poster path.

The poster URL is then displayed in the Streamlit application.

### API Key Security

The TMDB API key is stored in a local `.env` file and is not included in the source code or GitHub repository.

The `.env` file is excluded through `.gitignore`.

## 🎞️ TMDB Attribution

This product uses the TMDB API but is not endorsed or certified by TMDB.

Movie posters and related movie data are provided by TMDB.

## 🚀 Future Improvements

- Add user-based movie ratings and feedback
- Implement collaborative filtering
- Develop a hybrid recommendation system combining content-based and collaborative filtering
- Improve recommendation quality through feature weighting
- Add movie rating and genre filters
- Add movie details such as ratings, release date, and overview
- Improve the user interface and overall application design
- Deploy the application online

## 📚 Project Documentation

Detailed documentation of the project is available in the `docs/` folder.

The documentation covers:

- Project overview
- Dataset and data exploration
- Data preprocessing
- Feature engineering
- TF-IDF vectorization
- Cosine similarity
- Recommendation logic
- TMDB API integration
- Streamlit application
- Project structure
- Troubleshooting and security considerations

## 👨‍💻 Author

**Ujjawal Singhal**

B.Tech Computer Science & Engineering  
ABES Engineering College

- GitHub: [ujjawalsinghal](https://github.com/ujjawalsinghal)
- LinkedIn: [ujjawalsinghal](https://linkedin.com/in/ujjawalsinghal-dev)

## 📄 License

This project is intended for educational and academic purposes.