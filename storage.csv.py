import csv
from istorage import IStorage

class StorageCsv(IStorage):
    """Handles storing movie data in a CSV file."""

    def __init__(self, filename):
        self.filename = filename

    def list_movies(self):
        movies = {}
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row["title"]] = {
                        "year": int(row["year"]),
                        "rating": float(row["rating"]),
                        "poster": row["poster"]
                    }
        except FileNotFoundError:
            pass
        return movies

    def add_movie(self, title, year, rating, poster_url):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([title, year, rating, poster_url])

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["title", "year", "rating", "poster"])
                for movie, details in movies.items():
                    writer.writerow([movie, details["year"], details["rating"], details["poster"]])