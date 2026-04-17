# Dictionary to store movies
movies = {}

# Loop to get details of 3 movies
for i in range(1, 4):
    print(f"\nEnter details for Movie {i}:")
    title = input("Title: ").strip()
    director = input("Director: ").strip()
    year = input("Release Year: ").strip()
    rating = input("Rating: ").strip()
    
    #  To store in dictionary
    movies[title] = {
        "Director": director,
        "Release Year": year,
        "Rating": rating
    }

# Display movie information
print("\n--- Movie Details ---")
for title, details in movies.items():
    print(f"\nTitle       : {title}")
    print(f"Director    : {details['Director']}")
    print(f"Release Year: {details['Release Year']}")
    print(f"Rating      : {details['Rating']}")