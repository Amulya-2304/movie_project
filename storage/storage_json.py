import json
from istorage import IStorage

class StorageJson(IStorage):
    """Handles storing movie data in a JSON file."""

    def __init__(self, filename):
        self.filename = filename
        self._load_movies()

    def _load_movies(self):
        try:
            with open(self.filename, "r") as file:
                self.movies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.movies = {}

    def _save_movies(self):
        with open(self.filename, "w") as file:
            json.dump(self.movies, file, indent=4)

    def list_movies(self):
        return self.movies

    def add_movie(self, title, year, rating, poster_url):
        self.movies[title] = {"year": year, "rating": rating, "poster": poster_url}
        self._save_movies()

    def delete_movie(self, title):
        if title in self.movies:
            del self.movies[title]
            self._save_movies()
