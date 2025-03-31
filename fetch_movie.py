import requests

OMDB_API_KEY = "29a247c6"  # Replace with your actual API key
OMDB_URL = "http://www.omdbapi.com/"


def fetch_movie_data(title):
    """Fetch movie data from OMDb API."""
    params = {"apikey": OMDB_API_KEY, "t": title}

    try:
        response = requests.get(OMDB_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("Response") == "False":
            print(f"Error: {data.get('Error')}")
            return None

        return {
            "title": data.get("Title"),
            "year": data.get("Year"),
            "rating": data.get("imdbRating"),
            "poster": data.get("Poster"),
        }

    except requests.exceptions.RequestException as e:
        print(f"API request error: {e}")
        return None
