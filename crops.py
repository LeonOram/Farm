from wheat_class import *
from potato_class import *

def display_menu():
    print('''
Which crop would you like to create

1. Potato
2. Wheat

Please select an option
''')

def select_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected"))
            if choice in (1,2):
                valid = True
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

main()
