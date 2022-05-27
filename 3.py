class Tomato:
    states = {
        'appearance of seedlings': 0,
        'first true leaf': 1,
        'overgrowth of above-ground mass and roots': 2,
        'bud formation': 3,
        'flowering': 4,
        'fruit formation and ripening': 5
    }
    def __init__(self, index):
        self._index = index
        self._state = self.states[0]
    def grow(self):
        if self._state < 5:
            self._state += 1
    def is_ripe(self):
        if self._state == 5:
            return True
        return False
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]
        print(self.tomatoes)
    def grow_all(self):
        for tm in self.tomatoes:
            tm.grow()

    def all_are_ripe(self):
        return all([tm.is_ripe() for tm in self.tomatoes])
    def giv_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        self._plant.grow_all()
    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('not all ripe')

    @staticmethod
    def knowledge_base():
        print('gardener work')

Gardener.knowledge_base()
tomato_bush = TomatoBush(2)
gardener = Gardener(tomato_bush)
gardener.work()
gardener.harvest()