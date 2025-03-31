import json

DATA_FILE = "data.json"

def get_movies():
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    """
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            print("DEBUG: Loaded movies from JSON:", data)  # Debugging print
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("DEBUG: Error loading JSON:", e)  # Debugging error print
        return {}


def save_movies(movies):
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(movies, file, indent=4)

def add_movie(movie_name, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movies[movie_name] = {"year": year, "rating": rating}
    save_movies(movies)

def delete_movie(movie_name):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if movie_name in movies:
        del movies[movie_name]
        save_movies(movies)

def update_movie(movie_name, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    if movie_name in movies:
        movies[movie_name]["rating"] = rating
        save_movies(movies)
