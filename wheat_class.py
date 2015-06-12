from Crop import *

class Wheat(Crop):
    """Wheat!"""
    def __init__(self):
        super().__init__(1,2,2)
        self._type = "Wheat"

    def grow(self,light,water):
        if light >= self._light_need and water>=self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate *1.25
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate *1.5
            else:
                self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()
