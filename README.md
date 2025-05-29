
# 🎬 Movie Recommender System

A **content-based movie recommender system** built with Python and Streamlit that suggests movies based on their plot summaries. It uses **TF-IDF vectorization**, **cosine similarity**, and **TMDB API** to fetch movie posters — all served through an elegant web interface.

🔗 **Live Demo**: [movie-recommendationn.streamlit.app](https://movie-recommendationn.streamlit.app/)

---

## 🚀 Features

- 🔍 Recommend movies based on plot similarity
- 📚 Uses NLP with TF-IDF and cosine similarity
- 🖼️ Fetches movie posters using the TMDB API
- ⚡ Streamlit-based interactive web UI
- ✅ Clean and intuitive user experience

---

## 🗂️ Project Structure

```

📦 Movie Recommender System
├── App.py                      # Main Streamlit application
├── movies.pkl                  # Preprocessed movie metadata (LFS-tracked)
├── similarity.pkl              # Precomputed similarity matrix (LFS-tracked)
├── .env                        # API key storage (not pushed to GitHub)
├── requirements.txt            # Required Python packages
└── Movie-recommender-system.ipynb  # Development notebook

````

---

## 📂 Dataset

- **Source**: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Includes metadata: titles, overviews, genres, release dates, etc.

---

## 📷 Sample Output

When a user selects a movie (e.g., **"The Dark Knight"**), the system recommends:

- *Batman Begins*
- *The Dark Knight Rises*
- *Iron Man*
- *Man of Steel*
- *Avengers: Infinity War*

...along with their respective posters, fetched dynamically from TMDB.

---

## 🧠 Technologies Used

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Pandas**
- **Requests**
- **dotenv**
- **TMDB API**

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Yateeshapappala/Movie-recommender-System.git
cd Movie-recommender-System
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your TMDB API key

Create a `.env` file and add the following line:

```
TMDB_API_KEY=your_tmdb_api_key_here
```

> Ensure `.env` is excluded from Git with `.gitignore`.

### 4. Run the app locally

```bash
streamlit run App.py
```

---

## 📦 Large Files Handling

* `movies.pkl` and `similarity.pkl` are large files tracked using **Git LFS**.
* Ensure Git LFS is installed (`git lfs install`) before cloning and pushing changes.

---

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

```

Let me know if you'd like this saved directly to your `README.md` or want a version with deployment badges or GIF screenshots.
```
