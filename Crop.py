import random

class Crop:
    """A generic food crop"""

    def __init__(self,growth_rate,light_need,water_need):
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        return {"light need":self._light_need,"water need":self._water_need}

    def report(self):
        return {"type":self._type,"status":self._status,"growth":self._growth,"days growing":self._days_growing}

    def _update_status(self):
        if self._growth >15:
            self._status = "Old"
        elif self._growth >10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        else:
            self._status = "Seed"
        
    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()



def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

def manual_grow(crop):
    valid =False
    while not valid:
        try:
            light = int(input("Please input a light value (1-10): "))
            if 1 <= light <= 10:
                valid = True
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    valid = False
    while not valid:
        try:
            water = int(input("Please input a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    crop.grow(light,water)

def display_menu():
    print('''
1. Grow manually
2. Grow automaticlly (30 days)
3. Report status
0. Exit

Please select an option
''')

def get_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Option Selected: "))
            if 0 <= choice <= 4:
                valid = True
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")
    return choice

def manage_crop(crop):
    print("This is the crop management system")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(crop)
        elif option == 2:
            auto_grow(crop,30)
        elif option == 3:
            print(crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print("Goodbye")


#def main():
    #new_crop = Crop(1,4,3)
    #manage_crop(new_crop)

    

if __name__ == "__main__":
    main()
    
