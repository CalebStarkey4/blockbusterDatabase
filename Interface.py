from typing import Union
from datetime import date

# I'm going to have the app ask the user what they would like to do, with options to view, update, add, or delete an entry.
print("Welcome to the blockbuster movie library.")
keep_going = True
while keep_going:
    match enter_choice():
        case 1: # View a single entry
            search_type = str.lower(input("Would you like to search by ID number or title (ID/Title)? "))
            while True:
                if search_type == "id":
                    display(get_movies_by_id())
                    break
                elif search_type == "title":
                    display(get_movies_by_title())
                    break
                else:
                    search_type = input('Please enter either "ID" or "Title": ')
            break
        case 2: # Update an entry
            display(updateMovies())
            break
        case 3: # Add an entry
            display(addMovies())
            break
        case 4: # Delete an entry
            display(deleteMovies())
            break
        case 5: # View a subset of entries
            filter_options = ["year", "genre", "language", "rating"]
            filter_type = input(f"Which filter would you like to apply?\n{[f"{n} - {option}\n" for n, option in range(1, len(filter_options) + 1), filter_options]}")
            while True:
                match filter_type :
                    case 1:
                        display(get_movies_by_year())
                        break
                    case 2:
                        display(get_movies_by_genre())
                        break
                    case 3:
                        display(get_movies_by_language())
                        break
                    case 4:
                        display(get_moies_by_rating())
                        break
                    case _:
                        filter_type = input (f"Please enter the number for one of the given options:\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}\n")
            break
        case 6: # End the program
            keep_going = False
            break

def enter_choice() -> int:
    """A function that prompts the user for a choice and returns an integer 1-[option_count] to represent the chosen option, or 0 to indicate an error."""
    menu_options = ["View an entry", "Update an entry", "Add an entry", "Delete an entry", "View a subset of entries", "End the program"] 
    option_count = 6
    choice = input(f"What would you like to do?\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}")
    while True: # loop until a valid option has been selected
        if 1 <= choice <= option_count: # if a valid option has been selected
            return choice # breaks out of the loop
        else: # if the user input is an invalid selection
            choice = input (f"Please enter the number for one of the given options:\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}\n")

def get_movies_by_id() -> list:
    """Return a specific movie by ID."""
    movies = []
    while keep_going:
        id = input(f"Please enter the ID of the movie you're looking for: ")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_movies_by_year() -> list:
    """Returns all movies made in the given year"""
    movies = []
    while keep_going:
        min_year = input(f"Please enter the earliest year you want to see: ")
        max_year = input(f"\nPlase enter the latest year you want to see:")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_movies_by_genre() -> list:
    """Returns all movies of the given genre"""
    movies = []
    while keep_going:
        id = input(f"Please enter the : ")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_movies_by_language() -> list:
    """Returns all movies in the given language"""
    movies = []
    while keep_going:
        id = input(f"Please enter the ID of the movie you're looking for: ")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_moies_by_rating() -> list:
    """Returns all movies within a given range of ratings, or with a specific rating"""
    movies = []
    while keep_going:
        id = input(f"Please enter the ID of the movie you're looking for: ")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_movies_by_title() -> list:
    """Returns all movies whose titles contain the given string."""
    movies = []
    while keep_going:
        id = input(f"Please enter the ID of the movie you're looking for: ")
        movie_id = 1234
        movie_title = "This is a test"
        movie_year = date(2002)
        movie_genre = "This is a test"
        movie_language = "This is a test"
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def display(movies: list):
    """Displays movie or list of movies to the user from a list with the following structure: [id: int, title: str, year: datetime, genre: str, language: str]"""
    for movie in movies:
        print(f"{movie[0]} {movie[1]} {movie[2]} {movie[3]} {movie[4]}\n")