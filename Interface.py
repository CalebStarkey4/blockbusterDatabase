# I'm going to have the app ask the user what they would like to do, with options to view, update, add, or delete an entry.



def enterChoice() -> int:
    """A function that prompts the user for a choice and returns an integer 1-[option_count] to represent the chosen option, or 0 to indicate an error."""
    options = ["1 - View an entry", "2 - Update an entry", "3 - Add an entry", "4 - Delete an entry", "5 - View a subset of entries", "6 - End the program"] 
    option_count = 6
    choice = input(f"What would you like to do?\n{[f"{option}\n" for option in options]}")
    if 1 <= choice <= option_count: # if a valid option has been selected
        return choice
    else: # if the user input is an invalid selection
        while True:
            choice = input (f"What would you like to do?\n{[f"{option}\n" for option in options]}\n")
             

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