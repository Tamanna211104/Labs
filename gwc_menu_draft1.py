import time

def get_menu_options():
 menu_options = ('h','x','s')

 while True:
    print()
    print('** MENU **')
    print('h = help')
    print('x = exit')
    print('s = start')

    print()
    user_input = input('Enter an option:  ')
    if user_input in menu_options:
        return user_input

    else:
        print()
        print('Invalid option')

        # this is the basic code
        # from here on students can proceed to add details to their code such as:

user_input = get_menu_options()

if user_input == 's':
    print("Processing...")
    time.sleep(5)
    print()
    print('** RESULTS **')
    print('Results here')

elif user_input == 'h':
    print('** HELP **')
    print('Help text here')

elif user_input == 'x':
    print()
    print('See you soon')
    exit()

# to output different options type clear in the terminal
# students can experiment different things they can do with this code







