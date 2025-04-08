# Function to read movie data
def get_movie_data(storage):
    movies = storage.list_movies()  # List of movies from the storage
    movie_grid = ""

    # Create movie grid HTML
    for title, details in movies.items():
        movie_html = f"""
        <div class="movie">
            <img src="{details['poster']}" alt="{title}">
            <h2>{title}</h2>
            <p>Year: {details['year']}</p>
            <p>Rating: {details['rating']}</p>
        </div>
        """
        movie_grid += movie_html
    return movie_grid


# Function to generate the website
def generate_website(storage, template_path, output_path):
    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    movie_grid = get_movie_data(storage)  # Get movies data for the grid
    title = "My Movie Collection"  # You can change this to your app's title

    # Use string formatting to replace placeholders in the template
    rendered_html = template_content.replace('__TEMPLATE_TITLE__', title)
    rendered_html = rendered_html.replace('__TEMPLATE_MOVIE_GRID__', movie_grid)

    # Write the generated HTML to output_path
    with open(output_path, 'w') as output_file:
        output_file.write(rendered_html)

    print("Website was generated successfully.")


# Example usage:
# Assuming you have a `StorageJson` or `StorageCsv` storage implementation
from storage.storage_json import StorageJson

storage = StorageJson('.venv/static/data/movies.json')  # Replace with your storage
generate_website(storage, 'index.html', 'index.html')
