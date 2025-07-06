import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 1. Sample dataset
data = {
    'title': [
        'The Matrix', 'John Wick', 'Avengers: Endgame',
        'The Notebook', 'Titanic', 'La La Land',
        'Interstellar', 'Inception', 'The Dark Knight', 'Gravity'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality and his role in the war against its controllers.',
        'An ex-hit-man comes out of retirement to track down the gangsters that killed his dog.',
        'Superheroes assemble to undo the damage caused by Thanos.',
        'A romantic drama about a young couple in the 1940s.',
        'A romance that blossoms aboard the ill-fated Titanic.',
        'A jazz pianist falls for an aspiring actress in Los Angeles.',
        'A team of explorers travel through a wormhole in space to ensure humanity\'s survival.',
        'A thief who steals corporate secrets through use of dream-sharing technology.',
        'Batman battles the Joker in Gotham City.',
        'Astronauts struggle to survive after their space shuttle is destroyed.'
    ]
}

df = pd.DataFrame(data)

# 2. TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words='english')
df['description'] = df['description'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['description'])

# 3. Cosine similarity
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# 4. Index mapping
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# 5. Recommendation function with descriptions
def recommend(title, num_recommendations=5):
    if title not in indices:
        print(f"❌ Movie '{title}' not found in database.")
        return pd.DataFrame()
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    movie_indices = [i[0] for i in sim_scores]
    return df[['title', 'description']].iloc[movie_indices]

# 6. Display results
def display_recommendations(movie_title):
    print(f"\n🎯 Recommendations for '{movie_title}':\n")
    recommendations = recommend(movie_title)
    if recommendations.empty:
        return
    for index, row in recommendations.iterrows():
        print(f"🎬 {row['title']}")
        print(f"📝 {row['description']}\n")

# 7. Run
if __name__ == "__main__":
    display_recommendations("Inception")
    display_recommendations("Titanic")