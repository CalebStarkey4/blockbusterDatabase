# I'm going to have the app ask the user what they would like to do, with options to view, update, add, or delete an entry.
print("Welcome to the blockbuster movie library.")
keep_going = True
while keep_going:
    switch enterChoice():
        case 1: # View a single entry
            search_type = str.lower(input("Would you like to search by ID number or title (ID/Title)? "))
            while True:
                if search_type == "id":
                    display(getMoviesByID())
                    break
                elif search_type == "title":
                    display(getMoviesByTitle())
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
                switch filter_type :
                    case 1:
                        display(getMoviesByYear())
                        break
                    case 2:
                        display(getMoviesByGenre())
                        break
                    case 3:
                        display(getMoviesByLanguage())
                        break
                    case 4:
                        display(getMoviesByRating())
                        break
                    default:
                        filter_type = input (f"Please enter the number for one of the given options:\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}\n")
            break
        case 6: # End the program
            keep_going = False
            break

def enterChoice() -> int:
    """A function that prompts the user for a choice and returns an integer 1-[option_count] to represent the chosen option, or 0 to indicate an error."""
    menu_options = ["View an entry", "Update an entry", "Add an entry", "Delete an entry", "View a subset of entries", "End the program"] 
    option_count = 6
    choice = input(f"What would you like to do?\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}")
    while True: # loop until a valid option has been selected
        if 1 <= choice <= option_count: # if a valid option has been selected
            return choice # breaks out of the loop
        else: # if the user input is an invalid selection
            choice = input (f"Please enter the number for one of the given options:\n{[f"{n} - {option}\n" for n, option in range(1, len(menu_options) + 1), menu_options]}\n")

def getMoviesByID() -> list:
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

def deleteMovies() -> list:
    """Drops a record from the database"""
    return ["This", "is", "a", "test"]

def updateMovies() -> list:
    """Updates movie information in the database"""
    id = input("Please enter the ID of the movie you want to update: ")
    
    return ["This", "is", "a", "test"]

def addMovies():
    """Adds a movie or movies to the database"""

def display(movies: list):
    """Displays movie or list of movies to the user"""