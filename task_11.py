class Dessert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    @name.setter
    def name(self, name):
        self._name = name

    @calories.setter
    def calories(self, calories):
        self._calories = calories

    def is_healthy(self):
        return self._calories < 200 if isinstance(
            self._calories, int
        ) else False

    def is_delicious(self):
        return True
