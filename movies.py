import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Load and preprocess the dataset
def load_data(file_path='imdb_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()

# Vectorize the combined features and compute cosine similarity


# List all unique genres


# Recommend movies based on filters (genre, mood, rating)


# Display recommendations🍿 😊  😞  🎥

# Small processing animation


# Handle AI recommendation flow 🔍


    # Processing animation while analyzing mood 😊  😞  😐
    
    # Processing animation while finding movies
    
      # Small processing animation while finding movies 🎬🍿

   
# Main program 🎥
def list_genres(df):
    return sorted(set(genre.strip()for sublist in df['Genre'].dropna().str.strip(',') for genre in sublist))
genres=list_genres(movies_df)
def recommend_movies(genre=None,mood=None, rating=None, top_n=5):
    filtered_df = movies_df
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na= False)]
    if rating:
        filtered_df=filtered_df[filtered_df['IMDB_Rating']>=rating]
    filtered_df=filtered_df.sample(frac=1).reset_index(drop=True)
    recommendations=[]
    for idx,row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        polarity=TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity<0 and polarity>0) or polarity >=0)) or not mood:
            recommendations.append((row['Series_Title'], polarity))
        if len(recommendations)==top_n:
            break
    return recommendations if recommendations else "No suitable movie recommendations found."
def display_recommendations(recs, name):
    print(Fore.YELLOW +f"\n 🍿 AI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs,1):
        sentiment = "Positive 😃" if polarity > 0 else "Negative " if polarity <0 else "Neutral "
        print(f"{Fore.CYAN}{idx}. {title} (Polarity: {polarity: .2f}, {sentiment})")
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)