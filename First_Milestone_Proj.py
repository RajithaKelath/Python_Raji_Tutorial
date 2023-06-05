#Adding user input about movies to list

my_movie_list = []

def add_movie():
    add_more = 'y'
    while add_more == 'y':
        name = input("Enter movie name: ")
        director = input("Enter director name: ")
        year = input("Enter year of movie release: ")

        my_movie_dict = {"name" : name,
            "director" : director,
            "year" : year
            }
        

        my_movie_list.append(my_movie_dict)


        ask_user = input("Would you like to add more y/n: ")
        while ask_user.lower() not in ('y','n'):
            print("Try again y or n?")
            ask_user = input("Would you like to add more y/n: ")
            
        add_more = ask_user.lower()


#Listing all the movies 
def list_movie():
    print("******************************")
    for counter, movie in enumerate(my_movie_list):
       print(f"{counter} Name : {movie['name']},   Director : {movie['director']},   Year: {movie['year']}")
    
    print("******************************")

#searching all the movies 
def search_movie():
    new_movie_list = []
    user_search = input("Using which you would like to search? y for year/ d for director: ")

    if user_search.lower() == 'y':
        year_search = input("Enter year: ")
        for movie in my_movie_list:
            if movie['year'] == year_search:
                new_movie_list.append(movie['name'])
            
    elif user_search.lower() == 'd':
        director_search = input("Enter director name: ")
        for movie in my_movie_list:
            if (movie['director']).lower() == director_search.lower():
                new_movie_list.append(movie['name'])

    if len(new_movie_list) == 0:
        print("Oops! no result found")
    else:
        print("******************************")
        print(new_movie_list)
        print("******************************")

#check with user what operation they want to perform

MENU_PROMPT = "\nEnter a for adding movie \nEnter l for listing all movies \nEnter s for serching or \nEnter q for quitting \n"

slection = {
    "a" : add_movie,
    "l": list_movie,
    "s": search_movie
}

def main_prog():
    user_input = input(MENU_PROMPT)
    while user_input.lower() != "q":
        if user_input in slection:
            slection_item = slection[user_input]
            slection_item()
        else:
            print("unknow command. Try again!")
    
        user_input = input(MENU_PROMPT)
 

main_prog()
