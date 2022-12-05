# I'm going to have the app ask the user what they would like to do, with options to view, update, add, or delete an entry.

def enterChoice() -> int:
    """A function that prompts the user for a choice and returns an integer 1-[option_count] to represent the chosen option, or 0 to indicate an error."""
    option_count = 6
    choice = input("What would you like to do?\n1 - View an entry\n2 - Update an entry\n3 - Add an entry\n4 - Delete an entry\n5 - View a subset of entries\n6 - End the program\n")
    return choice if 1 <= choice <= option_count else 0

def getMoviesByID() -> str:
    """Return a specific movie by ID."""
    id = input(f"Please enter the ID of the movie you're looking for: ")
    return ["This", "is", "a", "test"]

def getMoviesByYear() -> list:
    """Returns all movies made in the given year"""
    return ["This", "is", "a", "test"]

def getMoviesByGenre() -> list:
    """Returns all movies of the given genre"""
    return ["This", "is", "a", "test"]

def getMoviesByLanguage() -> list:
    """Returns all movies in the given language"""
    return ["This", "is", "a", "test"]

def getMoviesByRating() -> list:
    """Returns all movies within a given range of ratings, or with a specific rating"""
    return ["This", "is", "a", "test"]

def getMoviesByTitle() -> list:
    """Returns all movies whose titles contain the given string."""
    return ["This", "is", "a", "test"]