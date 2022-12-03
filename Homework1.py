class Animal:
    species = "Tigers"

    def __init__(self, power, age, weight):
        self.power = power #0-100
        self.age = age #years
        self.weight = weight #kg


tiger = Animal(56, 12, 270)
print(tiger.species)
print(tiger.power)
print(tiger.age)
print(tiger.weight)
print("")


class Car:
    producer = "Renault"

    def __init__(self, max_speed, age, weight, model = "Logan"):
        self.max_speed = max_speed #km/h
        self.age = age #years
        self.weight = weight #kg
        self.model = model


car1 = Car(389, 4, 987)
print(car1.producer)
print(car1.max_speed)
print(car1.age)
print(car1.weight)
print(car1.model)