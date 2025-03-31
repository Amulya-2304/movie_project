from abc import ABC, abstractmethod

class IStorage(ABC):
    """Interface for movie storage classes."""

    @abstractmethod
    def list_movies(self):
        """Returns a dictionary containing movie data."""
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster_url):
        """Adds a movie to storage."""
        pass

    @abstractmethod
    def delete_movie(self, title):
        """Deletes a movie from storage."""
        pass
