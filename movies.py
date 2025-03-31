import random
import statistics

import movie_storage


def list_movies():
    """Lists all movies stored in the database."""
    movies = movie_storage.get_movies()
    if not movies:
        print("No movies found.")
        return

    for movie_name, details in movies.items():
        print(f"{movie_name} - Year: {details['year']}, Rating: {details['rating']}")


def add_movie():
    """Adds a new movie to the database."""
    movies = movie_storage.get_movies()
    movie_name = input("Enter new movie name: ")

    if movie_name in movies:
        print(f"Movie '{movie_name}' already exists!")
        return

    year = input("Enter release year: ")
    rating = input("Enter movie rating: ")

    movie_storage.add_movie(movie_name, int(year), float(rating))
    print(f"Movie '{movie_name}' successfully added.")


def delete_movie():
    """Deletes a movie from the database."""
    movie_name = input("Enter movie name to delete: ")

    movies = movie_storage.get_movies()
    if movie_name not in movies:
        print(f"Movie '{movie_name}' not found.")
        return

    movie_storage.delete_movie(movie_name)
    print(f"Movie '{movie_name}' deleted successfully.")


def update_movie():
    """Updates the rating of an existing movie."""
    movie_name = input("Enter movie name to update: ")

    movies = movie_storage.get_movies()
    if movie_name not in movies:
        print(f"Movie '{movie_name}' not found.")
        return

    new_rating = input("Enter new rating: ")
    movie_storage.update_movie(movie_name, float(new_rating))
    print(f"Movie '{movie_name}' updated successfully.")


def print_stats(movies):
    """Prints statistical information about the movies' ratings."""
    ratings = [details["rating"] for details in movies.values()]

    if not ratings:
        print("No movies to display stats.")
        return

    print(f"Average rating: {sum(ratings) / len(ratings):.2f}")
    print(f"Median rating: {statistics.median(ratings):.2f}")

    max_rating = max(ratings)
    min_rating = min(ratings)

    best_movies = [m for m, d in movies.items() if d["rating"] == max_rating]
    worst_movies = [m for m, d in movies.items() if d["rating"] == min_rating]

    print(f"Best movie(s) by rating: {', '.join(best_movies)}")
    print(f"Worst movie(s) by rating: {', '.join(worst_movies)}")


def random_movie(movies):
    """Selects and prints a random movie with its rating."""
    if movies:
        movie, details = random.choice(list(movies.items()))
        print(f"Random movie: {movie} ({details['year']}), Rating: {details['rating']}")
    else:
        print("No movies available.")


def search_movie(movies):
    """Searches for a movie by partial name and prints matches."""
    search_query = input("Enter part of the movie name: ").lower()
    matched = [(m, d) for m, d in movies.items() if search_query in m.lower()]

    if matched:
        for movie, details in matched:
            print(f"{movie} ({details['year']}): {details['rating']}")
    else:
        print("No movies found.")


def movies_sorted_by_rating(movies):
    """Prints movies sorted by rating in descending order."""
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["rating"], reverse=True)
    for movie, details in sorted_movies:
        print(f"{movie} ({details['year']}): {details['rating']}")


def main():
    """Main function that runs the movie management menu."""
    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Delete Movie")
        print("4. Update Movie")
        print("5. Stats")
        print("6. Random Movie")
        print("7. Search Movie")
        print("8. Movies Sorted by Rating")

        choice = input("Enter your choice: ")
        print()  # Add line gap after the choice input

        if choice == "0":
            print("Bye!")
            break
        elif choice == "1":
            list_movies()
        elif choice == "2":
            add_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            update_movie()
        elif choice == "5":
            movies = movie_storage.get_movies()
            print_stats(movies)
        elif choice == "6":
            movies = movie_storage.get_movies()
            random_movie(movies)
        elif choice == "7":
            movies = movie_storage.get_movies()
            search_movie(movies)
        elif choice == "8":
            movies = movie_storage.get_movies()
            movies_sorted_by_rating(movies)
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")  # Pause before showing menu again


if __name__ == "__main__":
    main()
