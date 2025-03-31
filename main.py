from movie_app import MovieApp
from storage.storage_json import StorageJson  # Or use StorageCsv

def main():
    storage = StorageJson(".venv/static/data/movies.json")  # Change to "movies.csv" for CSV
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
