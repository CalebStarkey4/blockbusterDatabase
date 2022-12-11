from typing import Union, List
from datetime import date, datetime
import Blockbuster as buster
import re

def confirm_choice(question: str = "Are you sure there are no more movies you want to see", default: str = 'n') -> bool:
    """Asks the user the given question, followed by " (y/n)? " with the default value capitalized. Returns True on a 'Y' or 'y' and False on a 'N' or 'n'.
    Any other value will be taken as the default value."""
    input_guide = "y/N" if default == 'n' else "Y/n"
    answer = str.lower(input(f"{question} ({input_guide})? "))
    if answer not in {'y', 'n'}:
        answer = default
    if answer == 'y':
        return True
    elif answer == 'n':
        return False

def enter_choice() -> int:
    """A function that prompts the user for a choice and returns an integer 1-[option_count] to represent the chosen option, or 0 to indicate an error."""
    menu_options = ["View an entry", "View a subset of entries", "End the program"] 
    nums = range(1, len(menu_options) + 1)
    option_string = [f"{n} - {option}\n" for n, option in zip(nums,menu_options)]
    choice = input(f"What would you like to do?\n{option_string}")
    while True: # loop until a valid option has been selected
        if 1 <= choice <= len(menu_options): # if a valid option has been selected
            return choice # breaks out of the loop
        else: # if the user input is an invalid selection
            choice = input(f"Please enter the number for one of the given options:\n{option_string}\n")

    

def get_movies_by_id() -> list:
    """Return a specific movie by ID."""
    movies = []
    id_list = set()
    print("Please enter the IDs of the movies you're looking for (enter -1 to stop giving inputs):")
    while keep_going:
        id = input(f"$ ")
        if id in id_list:
            print("You've already entered this ID number; please try again.")
        if id > 0:
            movie = buster.getRecord(id) # update this function call once the function is written
            movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
            movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
            movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
            movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
            movie_language = "This is a test" 
            movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
        elif id == -1:
            keep_going = confirm_choice()
        else:
            keep_going = confirm_choice("Invalid entry; are you sure you don't want to search by something else", 'y')
    return movies

def get_movies_by_year() -> list:
    """Returns all movies made in the given range of years"""
    movies = []
    while keep_going:
        min_year = int(input(f"Please enter the earliest year you want to see (if you don't want to restrict the lower end, input 1000): "))
        max_year = int(input(f"\nPlase enter the latest year you want to see (cannot be higher than current year):"))
        current_date = datetime.now()
        if 1000 <= min_year <= current_date.year:   
            movies_from_db = buster.filterRecord() # update this function call once the function is written
            keep_going = False
        
    for movie in movies_from_db:
        movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
        movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
        movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
        movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
        movie_language = "This is a test" # derive this from movie once I have access to its structure so I can parse it
        movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def get_movies_by_genre() -> list:
    """Returns all movies of the given genres"""
    movies = []
    id_list = set()
    genre_list = []
    print(f'''The genres in this database include {[f"{genre}, " for genre in genre_list[1:len(genre_list) - 1]]} and {genre_list[-1]}.
    Please enter the genres you're looking for (enter "done" to stop giving inputs):''')
    while keep_going:
        genre = str.lower(input(f"$ "))
        if genre in genre_list:
            movies_from_db = buster.filterRecord() # update this function call once the function is written
            for movie in movies_from_db:
                movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
                if movie_id not in id_list:
                    movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
                    movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    movie_language = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    id_list += movie_id
                    movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
        elif genre == "done":
            keep_going = confirm_choice()
        else:
            print("That genre is not in this database, please try again:")
    return movies

def get_movies_by_language() -> list:
    """Returns all movies in the given languages"""
    movies = []
    id_list = set()
    lang_list = []
    print(f'''The languages in this database include {[f"{lang}, " for lang in lang_list[1:len(lang_list) - 1]]} and {lang_list[-1]}.
    Please enter the languages you're looking for (enter "done" to stop giving inputs):''')
    while keep_going:
        lang = input(f"$ ")
        if lang in lang_list:
            movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
            if movie_id not in id_list:
                movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
                movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                movie_language = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                id_list += movie_id
                movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
        elif lang == "done":
            keep_going = confirm_choice()
        else:
            print("That language is not in this database, please try again:")
    return movies

def get_movies_by_rating() -> list:
    """Returns all movies with a given set of ratings, or with a specific rating"""
    movies = []
    id_list = set()
    rating_list = []
    print(f'''The ratings in this database include {[f"{rating}, " for rating in rating_list[1:len(rating_list) - 1]]} and {rating_list[-1]}.
    Please enter the ratings you're looking for below (enter "done" to stop giving inputs):''')
    while keep_going:
        rating = input(f"$ ")
        if rating in rating_list:
            movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
            if movie_id not in id_list:
                movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
                movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                movie_language = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                id_list += movie_id
                movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
        elif rating == "done":
            keep_going = confirm_choice()
        else:
            print("That rating is not in this database, please try again:")
    return movies

def parse_string(tokens: List(str), and_or: str) -> List(str):
    """takes a tokenized string and splits it around and_or, removing the and_or's in the process. Returns a list of strings."""
    str_list = []
    while and_or in tokens:
        stop_point = tokens.index(and_or)
        str_list.append(" ".join(tokens[:stop_point])) # join the tokens between the cursor and the AND/OR and put them into str_list
        tokens = tokens[stop_point + 1:] # remove the portion of tokens that has been added to str_list
    if len(tokens) > 0: # check to make sure the search string didn't end with AND/OR to avoid index out of bounds errors
        str_list.append(" ".join(tokens))
    return str_list


def get_movies_by_title() -> list:
    """Returns all movies whose titles contain the given string."""
    movies = []
    print("Please enter the title of the movie you're looking for (press Enter on a blank input to cancel):")
    while keep_going:
        title_str = input(f"$ ")
        if title_str == "":
            keep_going = confirm_choice("Are you sure you want to cancel")
        else:
            # parse user input with regular expressions to allow for the use of AND and OR in title search
            title_str_tokens = title_str.split() #tokenize the search string to make it easier to manage
            if "AND" in title_str_tokens and "OR" in title_str_tokens:
                print("Please use either AND or OR in your search, not both.")
            else:
                if "AND" in title_str_tokens:
                    and_or = "AND"
                elif "OR" in title_str_tokens:
                    and_or = "OR"
                else:
                    and_or = None
                str_list = title_str if and_or == None else []
                movies_from_db = buster.filterRecord() # update this function call once the function is written
                if movies_from_db == None:
                    keep_going = confirm_choice("We couldn't find any movies that match your search, would you like to search again")
                for movie in movies_from_db:
                    movie_id = 1234 # derive this from movie once I have access to its structure so I can parse it
                    movie_title = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    movie_year = date(2002) # derive this from movie once I have access to its structure so I can parse it
                    movie_genre = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    movie_language = "This is a test" # derive this from movie once I have access to its structure so I can parse it
                    movies += [movie_id, movie_title, movie_year, movie_genre, movie_language]
    return movies

def display(movies: list):
    """Displays movie or list of movies to the user from a list with the following structure: [id: int, title: str, year: datetime, genre: str, language: str]"""
    for movie in movies:
        print(" ".join(movie))

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
        case 2: # View a subset of entries
            filter_options = ["year", "genre", "language", "rating"]
            filter_string = [f"{n} - {option}\n" for n, option in zip(range(1, len(filter_options) + 1), filter_options)]
            filter_type = input(f"Which filter would you like to apply?\n{filter_string}")
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
                        display(get_movies_by_rating())
                        break
                    case _:
                        filter_type = input (f"Please enter the number for one of the given options:\n{filter_string}\n")
            break
        case 3: # End the program
            keep_going = confirm_choice("Are you sure you want to end the program")
            break