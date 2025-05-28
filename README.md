
# 🎬 Movie Recommender System

This project is a **content-based movie recommender system** that suggests similar movies based on their plot summaries. It uses TF-IDF vectorization and cosine similarity to understand and match movie overviews.

## 📁 Project Structure

- `Movie-recommender-system.ipynb` — Jupyter Notebook containing the full implementation of the recommender system.

## 📌 Features

- Recommends movies similar to a given title.
- Uses Natural Language Processing (NLP) techniques for text analysis.
- Employs TF-IDF and cosine similarity for content-based filtering.
- Based on movie overviews from a real-world movie dataset.

## 🧠 Technologies Used

- Python
- Pandas
- Scikit-learn
- NLTK
- Jupyter Notebook

## 📂 Dataset

- **Source**: [TMDB Movie Metadata Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- The dataset includes metadata such as titles, overviews, genres, release dates, etc.

> Make sure to download the dataset from the above link and place it in the same directory as the notebook before running.

## ▶️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. **Install required libraries**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

   Open `Movie-recommender-system.ipynb` and run the cells step by step.

## 📷 Sample Output

> When you enter a movie title (e.g., *The Dark Knight*), the system returns a list of similar movies like *Batman Begins*, *The Dark Knight Rises*, etc.

