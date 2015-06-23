class Animal:
    def __init__(self,growth_rate,food_need,water_need):
        self._weight = None
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = None
        self._type = "Animal"
        self._name = "Bob"

    def needs(self):
        return {"food need":self._food_need,"water need":self._water_need}

    def report(self):
        return {"name":self._name,"status":self._status,"type":self._type,"weight":self._weight,"days_growing":self._days_growing}

    def _update_status(self):
        if self._weight > 15:
            self._status = "Old"
        elif self._weight > 10:
            self._status = "Mature"
        elif self._weight > 5:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Baby"
        else:
            self._status = "Unborn"

    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate

