from animal_class import *
class Sheep(Animal):
    def __init__(self):
        super().__init__(2,3,2)
        self.type = "Sheep"

    def grow(self,food,water):
        if light >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

