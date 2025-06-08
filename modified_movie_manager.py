class Movie:
    def __init__(self, movie_id, title, director, release_year, genre):
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre

    def __str__(self):
        return f"ID: {self.movie_id}\nTitle: {self.title}\nDirector: {self.director}\nYear: {self.release_year}\nGenre: {self.genre}"

class MovieManager:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie_id, title, director, release_year, genre):
        if movie_id in self.movies:
            return False, "Movie ID already exists"
        
        try:
            release_year = int(release_year)
            if not 1888 <= release_year <= 2024:
                return False, "Invalid release year"
        except ValueError:
            return False, "Release year must be a number"

        self.movies[movie_id] = Movie(movie_id, title, director, release_year, genre)
        return True, "Movie added successfully"

    def view_all_movies(self):
        return "\n\n".join(str(movie) for movie in self.movies.values()) if self.movies else "No movies in the collection"

    def search_movie(self, title):
        found = [str(movie) for movie in self.movies.values() if title.lower() in movie.title.lower()]
        return "\n\n".join(found) if found else "No movies found with that title"

    def update_movie(self, movie_id, **updates):
        if movie_id not in self.movies:
            return False, "Movie not found"

        movie = self.movies[movie_id]
        
        if 'release_year' in updates:
            try:
                year = int(updates['release_year'])
                if not 1900 <= year <= 2026:
                    return False, "Invalid release year"
                movie.release_year = year
            except ValueError:
                return False, "Release year must be a number"

        for key, value in updates.items():
            if value and key != 'release_year':
                setattr(movie, key, value)

        return True, "Movie updated successfully"

    def delete_movie(self, movie_id):
        if movie_id not in self.movies:
            return False, "Movie not found"
        
        del self.movies[movie_id]
        return True, "Movie deleted successfully"

def display_menu():
    print("\n=== Movie Management System ===")
    print("1. Add a new movie")
    print("2. View all movies")
    print("3. Search movies by title")
    print("4. Update movie information")
    print("5. Delete a movie")
    print("6. Exit")
    print("============***==============")

def main():
    manager = MovieManager()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            while True:
                movie_id = input("Enter movie ID: ")
                if movie_id in manager.movies:
                    print("Movie ID already exists. Please try a different ID.")
                    continue
                break
                
            title = input("Enter movie title: ")
            director = input("Enter director name: ")
            release_year = input("Enter release year: ")
            genre = input("Enter genre: ")
            print(manager.add_movie(movie_id, title, director, release_year, genre)[1])

        elif choice == "2":
            print(manager.view_all_movies())

        elif choice == "3":
            title = input("Enter movie title to search: ")
            print(manager.search_movie(title))

        elif choice == "4":
            movie_id = input("Enter movie ID to update: ")
            updates = {
                'title': input("New title (Enter to skip): "),
                'director': input("New director (Enter to skip): "),
                'release_year': input("New release year (Enter to skip): "),
                'genre': input("New genre (Enter to skip): ")
            }
            updates = {k: v for k, v in updates.items() if v}
            print(manager.update_movie(movie_id, **updates)[1])

        elif choice == "5":
            movie_id = input("Enter movie ID to delete: ")
            print(manager.delete_movie(movie_id)[1])

        elif choice == "6":
            print("Thank you for using the Movie Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 