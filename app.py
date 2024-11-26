import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_title):
    response = requests.get('http://www.omdbapi.com/?t={}&apikey=16edd8c9'.format(movie_title))
    data = response.json()
    print(data)
    return data['Poster']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_title = movies.iloc[i[0]].title

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_title))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'search movie or use drop down to select any',
    movies['title'].values
)

# Set the title with the new dark background
st.markdown('<p class="title">Movie Recommendation System</p>', unsafe_allow_html=True)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Define the maximum character length for the movie title to avoid overflow
    # max_title_length = 20
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0], use_container_width=True)
        st.markdown(
            f"<h5 style='text-align: center; color: black; font-size: 12px;'>{names[0]}",
            unsafe_allow_html=True)

    with col2:
        st.image(posters[1], use_container_width=True)
        st.markdown(
            f"<h5 style='text-align: center; color: black; font-size: 12px;'>{names[1]}",
            unsafe_allow_html=True)

    with col3:
        st.image(posters[2], use_container_width=True)
        st.markdown(
            f"<h5 style='text-align: center; color: black; font-size: 12px;'>{names[2]}",
            unsafe_allow_html=True)

    with col4:
        st.image(posters[3], use_container_width=True)
        st.markdown(
            f"<h5 style='text-align: center; color: black; font-size: 12px;'>{names[3]}",
            unsafe_allow_html=True)

    with col5:
        st.image(posters[4], use_container_width=True)
        st.markdown(
            f"<h5 style='text-align: center; color: black; font-size: 12px;'>{names[4]}",
            unsafe_allow_html=True)
