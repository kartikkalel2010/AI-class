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
def load_data(file_path='D:\github\AI-class\AI class 6\imdb_top_1000.csv'):
    try:
        df = pd.read_csv(file_path)
        df['combined_features'] = df['Genre'].fillna('') + ' ' + df['Overview'].fillna('')
        return df
    except FileNotFoundError:
        print(Fore.RED + f"Error: The file '{file_path}' was not found.")
        exit()

movies_df = load_data()

# Vectorize the combined features and compute cosine similarity
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies_df['combined_features'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


# jscbbvgfvjfdnj
# List all unique genres
def list_genres(df):
    return sorted(set(genre.strip() for sublist in df['Genre'].dropna().str.split(',') for genre in sublist))

# Example usage: genres = list_genres(movies_df)

# Recommend movies based on filters (genre, mood, rating)
def recommend_movies(genre=None, mood=None, rating=None, top_n=5):
    filtered_df = movies_df

    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]

    if rating:
        filtered_df = filtered_df[filtered_df['IMDB_Rating'] >= rating]

    filtered_df = filtered_df.sample(frac=1).reset_index(drop=True)  # Randomize the order

    recommendations = []
    for idx, row in filtered_df.iterrows():
        overview = row['Overview']
        if pd.isna(overview):
            continue
        
        polarity = TextBlob(overview).sentiment.polarity
        if (mood and ((TextBlob(mood).sentiment.polarity < 0 and polarity > 0) or polarity >= 0)) or not mood:
            recommendations.append((row['Series_Title'], polarity))
            if len(recommendations) == top_n:
                break

    return recommendations if recommendations else "No suitable movie recommendations found."

#fghjsdftrewazxcvhjk
# Initialize colorama for colored text
init()

# Display recommendations
def display_recommendations(recs, name):
    print(Fore.YELLOW + f"\nAI-Analyzed Movie Recommendations for {name}:")
    for idx, (title, polarity) in enumerate(recs, 1):
        sentiment = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
        print(f"{Fore.CYAN}[{idx}]. {title} (Polarity: {polarity:.2f}, {sentiment})")

# Small processing animation
def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)

# Handle AI recommendation flow
def handle_ai(name):
    print(Fore.BLUE + f"\n🔍 Let's find the perfect movie for you!\n")
    
    # Show genres in a single line
    print(Fore.GREEN + "AVAILABLE GENRES: ", end="")
    genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller", "Adventure", "Fantasy", "Mystery"]
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}[{idx}]. {genre}", end=" ")
    print()  # To move to the next line after all genres are listed

    while True:
        genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input) - 1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()

    # For demonstration, let's assume some mock recommendations based on genre and mood
    # In a real application, you'd query a database or API here
    mock_recommendations = [
        ("The Matrix", 0.8),  # Example: (title, polarity)
        ("Inception", 0.6),
        ("Interstellar", 0.4)
    ]

    # Display the mock recommendations
    display_recommendations(mock_recommendations, name)
    processing_animation()

# Example usage
if __name__ == "__main__":
    user_name = "User"  # You can modify this to take user input if needed
    handle_ai(user_name)

#fghjkhgfghjkllkgjklkjhg

def processing_animation():
    """Display a simple processing animation"""
    for _ in range(3):
        for char in '...':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write('\b\b\b   \b\b\b')  # Clear the dots

def recommend_movies(genre, mood, rating=None, top_n=5):
    """
    Placeholder function for movie recommendations.
    In a real implementation, this would query a database or API.
    """
    # This is just a mock implementation
    movies = [
        {"title": "The Shawshank Redemption", "rating": 9.3, "genre": "Drama", "mood": "positive"},
        {"title": "The Godfather", "rating": 9.2, "genre": "Crime", "mood": "neutral"},
        {"title": "The Dark Knight", "rating": 9.0, "genre": "Action", "mood": "positive"},
        {"title": "Pulp Fiction", "rating": 8.9, "genre": "Crime", "mood": "neutral"},
        {"title": "Fight Club", "rating": 8.8, "genre": "Drama", "mood": "negative"},
    ]
    
    # Filter movies based on criteria
    filtered = [m for m in movies if m["genre"].lower() == genre.lower()]
    if mood:
        filtered = [m for m in filtered if m["mood"] == mood.split()[0].lower()]
    if rating:
        filtered = [m for m in filtered if m["rating"] >= rating]
    
    return filtered[:top_n] if filtered else "No movies found matching your criteria."

def display_recommendations(movies, name):
    """Display the movie recommendations"""
    print(Fore.GREEN + f"\nHere are your movie recommendations, {name}:\n")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} (Rating: {movie['rating']})")

# Example usage (you would get these inputs from the user in a real implementation)
name = "User"  # This would come from earlier in the program
genre = "Drama"  # This would come from earlier in the program
modal = "I'm feeling happy today"  # This would come from user input

# Analyze mood
print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
processing_animation()  # Small processing animation during mood analysis
polarity = TextBlob(modal).sentiment.polarity
mood_desc = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
print(f"{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

# Get rating input
while True:
    rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
    if rating_input.lower() == 'skip':
        rating = None
        break
    try:
        rating = float(rating_input)
        if 7.6 <= rating <= 9.3:
            break
        print(Fore.RED + "Rating out of range. Try again.\n")
    except ValueError:
        print(Fore.RED + "Invalid input. Try again.\n")

# Find and display movies
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
processing_animation()  # Small processing animation while finding movies

recs = recommend_movies(genre=genre, mood=mood_desc, rating=rating, top_n=5)
if isinstance(recs, str):
    print(Fore.RED + recs + "\n")
else:
    display_recommendations(recs, name)

    #234567890asdfghjklxcvbnm,cvbnm,

def processing_animation():
    """Display a simple processing animation"""
    for _ in range(3):
        for char in '...':
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
    sys.stdout.write('\b\b\b   \b\b\b')  # Clear the dots

def recommend_movies(genre, mood, rating=None, top_n=5):
    """
    Placeholder function for movie recommendations.
    In a real implementation, this would query a database or API.
    """
    # This is just a mock implementation
    movies = [
        {"title": "The Shawshank Redemption", "rating": 9.3, "genre": "Drama", "mood": "positive"},
        {"title": "The Godfather", "rating": 9.2, "genre": "Crime", "mood": "neutral"},
        {"title": "The Dark Knight", "rating": 9.0, "genre": "Action", "mood": "positive"},
        {"title": "Pulp Fiction", "rating": 8.9, "genre": "Crime", "mood": "neutral"},
        {"title": "Fight Club", "rating": 8.8, "genre": "Drama", "mood": "negative"},
        {"title": "Inception", "rating": 8.8, "genre": "Sci-Fi", "mood": "neutral"},
        {"title": "The Matrix", "rating": 8.7, "genre": "Sci-Fi", "mood": "positive"},
        {"title": "Parasite", "rating": 8.6, "genre": "Drama", "mood": "negative"},
    ]
    
    # Filter movies based on criteria
    filtered = [m for m in movies if m["genre"].lower() == genre.lower()]
    if mood:
        filtered = [m for m in filtered if m["mood"] == mood.split()[0].lower()]
    if rating:
        filtered = [m for m in filtered if m["rating"] >= rating]
    
    return filtered[:top_n] if filtered else "No movies found matching your criteria."

def display_recommendations(movies, name):
    """Display the movie recommendations"""
    print(Fore.GREEN + f"\nHere are your movie recommendations, {name}:\n")
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} (Rating: {movie['rating']})")

def handle_ai(name):
    """Handle the movie recommendation process"""
    # Get genre input
    while True:
        genre = input(Fore.YELLOW + "What genre are you interested in? ").strip()
        if genre:
            break
        print(Fore.RED + "Genre cannot be empty. Try again.\n")

    # Get mood input
    modal = input(Fore.YELLOW + "How are you feeling today? (Tell us in a sentence): ").strip()
    
    # Analyze mood
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(modal).sentiment.polarity
    mood = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    print(f"{Fore.GREEN}Your mood is {mood} (Polarity: {polarity:.2f}).\n")

    # Get rating input
    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    # Get initial recommendations
    print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
    processing_animation()
    
    recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommendations(recs, name)

    # Ask for more recommendations
    while True:
        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 無 負 \n")
            break
        elif action == 'yes':
            recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
            if isinstance(recs, str):
                print(Fore.RED + recs + "\n")
            else:
                display_recommendations(recs, name)
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")

def main():
    print(Fore.BLUE + "無 Welcome to your Personal Movie Recommendation Assistant! 無\n")
    name = input(Fore.YELLOW + "What's your name? ").strip()

    print(f"{Fore.GREEN}Great to meet you, {name}!\n")
    handle_ai(name)

if __name__ == "__main__":
    main()