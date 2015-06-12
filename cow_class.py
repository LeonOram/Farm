from animal_class import *
class Cow(Animal):
    def __init__(self):
        super().__init__(1,4,4)
        self.type = "Cow"

    def grow(self,food,water):
        if light >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()
