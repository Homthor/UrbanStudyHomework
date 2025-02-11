from random import randint


class Animal:
    def __init__(self, speed):
        self.live = True
        self.sound = None
        self._DEGREE_OF_DANGER = 0
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        cords_d = [dx, dy, dz]
        new_cords = self._cords[:]
        for i in range(len(new_cords)):
            new_cords[i] += cords_d[i] * self.speed
        if new_cords[2] < 0:
            print(f"It's too deep, i can't dive :( {new_cords}")
        else:
            self._cords = new_cords

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(self.sound)
        else:
            print("No sound")


class Bird(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 5

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * (self.speed / 2)
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
        else:
            print(self._cords)


class PoisonousAnimal(Animal):
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


# print(Duckbill.mro())
db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
