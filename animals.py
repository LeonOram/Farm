from cow_class import *
from sheep_class import *

def display_menu():
    print('''
Please select an animal to raise
1. Cow
2. Sheep
''')

def get_animal_selection():
    valid = False
    try:
        while valid = False
        selection = int(input("Selection: "))
        if selection in [1,2]:
            valid = True
        else:
            print("Invalid")        
    except ValueError:
        print("Invalid")
    return selection

def instantiate_animal(selection):
    if selection == 1:
        animal = Cow()
    elif selection == 2:
        animal = Sheep()
    return animal

def display_main_menu():
    print('''
Main Menu
1. Manual Grow
2. Automatic Grow
3. Report
0. Quit
''')

def get_main_menu_selection():
    valid=False
    try:
        while not valid:
            selection = int(input("Selection: "))
            if selection in [1,2]:
                valid = True
            else:
                print("Invalid")
    except ValueError:
        print("Invalid")
