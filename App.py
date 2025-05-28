import streamlit as st
import pickle
import requests
import time
import os
from dotenv import load_dotenv 

load_dotenv() 

# --- Load data ---
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Use API key from .env ---
API_KEY = os.getenv("TMDB_API_KEY")

# --- Fetch poster with retry and fallback ---
def fetch_poster(movie_id, retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            else:
                break  # No poster path found
        except requests.exceptions.RequestException as e:
            #print(f"Attempt {attempt + 1}: Error fetching poster for ID {movie_id}: {e}")
            time.sleep(1)  # brief pause before retry
    return "https://via.placeholder.com/300x450?text=No+Image"

# --- Recommend movies based on similarity ---
def recommend(movie):
    match = movies[movies['title'] == movie]
    if match.empty:
        return [], []

    movie_index = match.index[0]
    distances = similarity[movie_index]
    movie_scores = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_scores:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# --- Streamlit App UI ---
st.title('🎬 Movie Recommender System')

movie_list = movies['title'].values
option = st.selectbox('Search for a movie:', movie_list)

if st.button('Recommend'):
    names, posters = recommend(option)
    if names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])
    else:
        st.warning("No recommendations found. Please select a valid movie.")
