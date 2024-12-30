from time import sleep

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def go_to(self, floor_required):
        if self.floors >= floor_required >= 1:
            for current_floor in range(floor_required):
                print('Этаж', current_floor + 1)
                sleep(1)
        else:
            print('Такого этажа не существует для:', self.name)


h1 = House('ЖК Эльбрус', 30)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)
