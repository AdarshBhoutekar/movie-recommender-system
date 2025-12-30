import streamlit as st
import pickle
import requests
import pandas as pd
import os
# Load files
movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def compute_similarity(movies):
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()
    similarity = cosine_similarity(vectors)
    return similarity

similarity = compute_similarity(movies)

import requests

API_KEY = os.getenv("TMDB_API_KEY")
# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=9fc685faba38608c82a9b43bac398993&language=en-US"
#     response = requests.get(url)
#     data = response.json()
#
#     return "https://image.tmdb.org/t/p/w500" + data["poster_path"]

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)   # timeout added
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Image"

    except Exception:
        # Handles ConnectionResetError, timeout, API down, etc.
        return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie):
    if movie not in movies['title'].values:
        return []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_poster =[]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch movie poster..
        recommended_movies.append(movies.iloc[i[0]]['title'])
        recommended_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_poster


# ---------- FRONTEND ----------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select Movie:",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    st.subheader("Recommended Movies")

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

