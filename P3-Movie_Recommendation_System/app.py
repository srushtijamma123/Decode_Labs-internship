import streamlit as st 
import pandas as pd
from movies import movies

df = pd.DataFrame(movies)
st.set_page_config(
    page_title="AI Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)
st.title("🎬 AI Movie Recommendation System")
st.markdown("--------")
st.info("Select your preferences from the sidebar and click'Recommend Movies'.")
st.sidebar.header("choose your preferences")
genres = sorted(
    set(
        genre
        for genre_list in df["genre"]
        for genre in genre_list
    )
)
selected_genre = st.sidebar.selectbox("Select Genre",genres)
languages = sorted(df["language"].unique())
selected_language = st.sidebar.selectbox("Select Language",languages)
moods = sorted(
    set(
        mood
        for mood_list in df["mood"]
        for  mood in mood_list
    )
)
selected_mood = st.sidebar.selectbox("Select Mood",moods)
search_movie = st.sidebar.text_input("🔍Search Movie")
recommend = st.sidebar.button("Recommend Movies")
if recommend:
    recommended_movies = []

    for movie in movies:

       if (
                selected_genre in movie["genre"]
                and selected_language == movie["language"]
                and selected_mood in movie["mood"]
                and (
                      search_movie == ""
                     or search_movie.lower() in movie["name"].lower()
    )
        ):
           recommended_movies.append(movie)
       

    if recommended_movies:
        st.success(f"🥳Found {len(recommended_movies)}movie(s)matching your preferences!")
        st.subheader("🎬 Recommended Movies")

        for movie in recommended_movies:

         st.markdown(f"## 🎬 {movie['name']}")

         st.write(f"⭐ Rating : {movie['rating']}")

         st.write(f"🌍 Language : {movie['language']}")

         st.write(f"🎭 Genre : {', '.join(movie['genre'])}")

         st.write(f"😊 Mood : {', '.join(movie['mood'])}")

         st.write(f"📝 {movie['description']}")

         st.divider()
    else:
        st.error("😔 No movies found!")

        st.info("Try selecting a different Genre, Language or Mood.")