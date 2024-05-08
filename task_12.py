from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=0, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        self._flavor = flavor

    def is_delicious(self):
        if self._flavor == 'black licorice':
            return False
        return super().is_delicious()
