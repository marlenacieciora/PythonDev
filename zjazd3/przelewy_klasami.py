#atrybuty kazdego krokodyla na swiecie (każdy krokodyl ma ogon)
class Crocodile:
    tail = True
    limbs = 4

#atrybuty konkretnego krokodyla (nie każdy krokodyl bedzie Andrzej)

    #metoda dunder????
    def __init__(self, name, place_of_habitat):
        self.name = name
        self.place = place_of_habitat

    # __ magiczna meto
  #w ramach klasy jest metoda
    def method(self):
        pass

#poza klasą funkcja
def function(self):
    pass

andrzej = Crocodile("Andrzej","ZOO in Wroclaw")
blazej = Crocodile("Blazej","Amazon forest")


@staticmethod
def get_population_count():
    pass