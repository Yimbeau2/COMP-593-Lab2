'''
Description: a complex data structure with some functions displaying some methods to work with the data structure.

Usage: python lab2_script_template.py

Author: Jimbeau
                               .-=-:.                          ..-=-.                               
                                 ..-+*:                     .:+=-..                                 
                               .... .:#-                   .=+.. .::.                               
                               .=#:. .:*=.                .=+.. .:#-.                               
                                .+*.  .:*%+:.          .:+#+..  .*+.                              ..
                                 :#:      .-#%*     .#%#-.      :#.                              ...
     ....:-*%%%%%%%=:....        .+%:.     ..%%%###%%%*.      .:%=         ....:=#%%%%%%#=::...     
 ...-*%##*-..     .-##%#=:..      .=%*..  .-%#.     .-#%:.  ..*%-       ..:-#%#*-.     ..-*#%%*-... 
.=##+:..              ..=*%%+-...   .*%=..=%:...::::...+#:..-#*.   ...-=%#*=..              ..:+#%=.
*%:.                      ..=*##+-.. .-#*:*#+#%#****#%#=%+:*#:. ..-=##*-..                      .:#*
=%=.                         ...=*%#+-..+%%#=..      ..+#%#=..-=##+-..                          .-#-
.=%+:.                            .:=*%#*#+....:-----:...+%*##+=..                            .:+#=.
 .:+##=..          ....:-==++++*******+*%%##%#*+====++*%%#%%*++******++++==-:.....         ..-*#+.. 
   ..-*%#*-.....-*#%%#*+==---::::::::::=##-...        ...-#%=::::::::::---==+*#%%#*=.....-+#%+-..   
     ....:+#%%%%=:......            ..*%*:.              .:*%*..            ......:+%%%%#+:...      
            .:#+.                 .-%%+%+.                .+#*%%=.                ..+#:.            
             .=%+..         ....-#%#*%%#%=...          ...-%%%%+#%#-....         ..=#=.             
              .:*%*-.......:-+%#*+#%+.-#%%%=:..........:=#%%%-:*%#+*%%*-:.......:+%*:.              
                ..=*#%%%%%#*+-.-**:.:*%#%+-+#%%#*++*#%%#+-+%#%#:.-*#-.-+*#%%%%%#*-..                
                    ....... ..+*:.:*%++#-.  .....::....   .-#*+%*:.:#+:. ......                     
                           .-#=. .*+.*#:.                  .:#*.+#...=#-.                           
                          .**:. .++.*%*=:....        .....:=+#%*.**. .:**.                          
                         .*-.  .+*::%%%%%%%#**********#%%%%%%%%%::*+.  .=#.                         
                       .:*:.  .=*-.=%=+%%%%%%%%%%%%%%%%%%%%%*-=%-.:#=.  .-#:                        
                       :*-.  .:*-. -%-.....::::-----::::..... -%: .-#-.  .-*:                       
                      :+-.   .=+.  .%*.                      .*%.  .==.  ..-*:.                     
                            .:*:    -%+...                ...=%:    :*-.   ....                     
                            .=+.     =%*-:................:=*%-.    .+=..                           
..                          :*:      .-%%%%%%%%%%%%%%%%%%%%%%-.      :*:.                           
..                         .=*.       .:#%%%%%%%%%%%%%%%%%%#:.       .+=.                           
..                         .#:          .=#*-.:::::::..:*#=.          :#:                           
'''

def main():

    #a complex data structure named about_me

    about_me = {

#full_name, student_id and a list named pizza_toppings obviously including (3) pizza toppings
    #__ Keys ______ Values ________
    'full_name': 'Jonathan Sproule',

    'student_id': 'SIERRA117',

    'pizza_toppings': ['HOTSAUCE', 'CHEESE', 'PEPPERS'], 

# a list of dictionaries (2) containing movie details
    'movies': [
        #____ Keys ______ Values _______
            {'title': 'harry potter',
             
            'genre': 'fantasy'},
            
            {'title': 'ferrari vs ford',
             
            'genre': 'drama documentary'},
            ]
    }

    # Calling First print statment function; prints students full name, then first name then Student ID
    print_student_name_and_id(about_me)
    
    # first print_pizza_toppings call
    print_pizza_toppings(about_me)


    # Calling function to add more pizza toppings to pizza_toppings
    add_pizza_toppings(about_me,toppings=('JALAPENOS', 'EXTRACHEESE', 'BACON')) 


    # Add another movie to the data structure
    about_me['movies'].append({'title':'fantastic beasts And where to find them', 'genre':'fantasy'})

    # second print pizza_toppings call
    print_pizza_toppings(about_me)

    #print movies genres
    print_movie_genres(about_me)

    print_movie_titles(about_me)



#: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):

    #afformentioned function
    last_name = about_me['full_name'].split()
    print(f"\nMy name is {about_me['full_name']}, but you can call me MCPO {last_name[1]}.\nMy student ID is {about_me['student_id']}")
    print()
    return
    
#: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me,toppings):

    for topping in toppings:
        topping = topping.lower()
        about_me['pizza_toppings'].append(topping)
    return

#: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):

    print(f"My favorite pizza toppings are:")

    # sort pizza toppings
    about_me['pizza_toppings'].sort()

    #iterates over each topping in pizza_toppings
    for topping in about_me['pizza_toppings']:
        
        #prints a dash then an individual topping 
        print(f"- {topping}")
    print()
    return

# Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):

    print(f"I like to watch", end= " ")

    i = 0

    while i != 3:
        if i == 2:
            print(f"and {about_me['movies'][i]['genre']} movies.")
            
        else:
            print(f"{about_me['movies'][i]['genre']},", end=" ")
        i += 1

    #new_list = about_me['movies'][0]['genre'], about_me['movies'][1]['genre'],  about_me['movies'][2]['genre']
    #print(f"I like to watch {new_list}"      

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    
    print(f"\nSome of my favorite movies are ", end="")

    i = 0
    while i != 3:

        if i == 2:

            print(f"and {movie_list['movies'][i]['title'].title()}.")
            return

        else:
        
            print(f"{movie_list['movies'][i]['title'].title()},", end= " ")
            i += 1
    
    
    
    return
    
if __name__ == '__main__':
    main()