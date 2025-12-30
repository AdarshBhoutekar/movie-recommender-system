# 🎬 Movie Recommender System

A content-based movie recommender system that suggests similar movies based on movie metadata and displays posters using the TMDB API.

**Live Demo:**  
https://movie-recommender-system-flulzcthmmyscqxk3zzy36.streamlit.app/

---

##  Features
- Recommends similar movies using **content-based filtering**
- Uses **cosine similarity** on movie tags
- Displays movie posters fetched from **TMDB API**
- Simple and interactive **Streamlit web interface**
- Deployed online using **Streamlit Cloud**

---

##  Tech Stack
- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **TMDB API**

---

##  How It Works
1. Movie metadata is processed to create textual tags  
2. Tags are vectorized using `CountVectorizer`  
3. Cosine similarity is used to find similar movies  
4. Similarity is computed dynamically and cached  
5. Movie posters are fetched using TMDB API  

---

##  How to Use (Online)
1. Open the live demo link  
2. Select a movie from the dropdown  
3. Click **Recommend**  
4. View recommended movies along with posters  

---

##  Run Locally (Optional)

### Clone the repository
```bash
git clone https://github.com/<your-username>/movie-recommender-system.git
cd movie-recommender-system

Adarsh  
B.Tech (AI & ML) Student
