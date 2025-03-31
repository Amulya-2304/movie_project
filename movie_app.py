from website_generator import generate_website
from fetch_movie import fetch_movie_data  # ✅ Add this
  # ✅ Add this line


class MovieApp:
    """Main movie application class."""

    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """List all stored movies."""
        movies = self._storage.list_movies()
        if movies:
            for title, details in movies.items():
                print(f"{title} ({details['year']}) - {details['rating']}/10")
        else:
            print("No movies found.")

    def _command_add_movie(self):
        """Add a new movie using OMDb API."""
        title = input("Enter movie title: ")
        movie_data = fetch_movie_data(title)

        if movie_data:
            self._storage.add_movie(
                movie_data["title"],
                movie_data["year"],
                movie_data["rating"],
                movie_data["poster"]
            )
            print(f"Movie '{movie_data['title']}' added successfully!")
        else:
            print("Failed to add movie.")

    def _command_delete_movie(self):
        """Delete a movie from storage."""
        title = input("Enter movie title to delete: ")
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted.")

    def _command_generate_website(self):
        """Generate the movie website."""
        movies = self._storage.list_movies()
        generate_website(movies)

    def run(self):
        """Main loop for the app."""
        while True:
            print("\n1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("9. Generate website")
            print("0. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "9":
                self._command_generate_website()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
