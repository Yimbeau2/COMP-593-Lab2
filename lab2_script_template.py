def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {

    'full_name': 'Jonathan Sproule',

    'student_id': '69696969699',

    'pizza_toppings': { 'PINEAPPLE', 'CHEESE', 'PEPPERS' }, 

    'movies': [

            {'title': ' Harry Potter',
             
            'genre': ' fantasy'},
            
            {'title': 'Ferrari vs Ford',
             
            'genre': 'drama doc'}
            ]
    }

    # Calling First print statment function
    print_student_name_and_id(about_me)


    # Calling function to add more pizza toppings
    add_pizza_toppings(about_me,[toppings: 'ONIONS', 'EXTRA CHEESE', 'BACON'] ) 


    # TODO: Step 3 - Add another movie to the data structure

    about_me['movies'] = {'title': 'Fantastic Beasts And Where To Find Them'}


# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):

    print(f"My name is {about_me: [full_name]}, but you can call me Lord {about_me: [full_name.split()]}")

    print(f"My student ID is {about_me:[student_id]}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):

    about_me[toppings] = [toppings.split()]

    about_me[toppings] = [list.sort([toppings])]

    about_me[toppings] = [toppings.lower()]

    about_me[toppings] = [toppings.append(toppings)]

    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()