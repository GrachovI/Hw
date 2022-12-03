class Animal:
    species = "Tiger"

    def __init__(self, power, age, weight):
        self.power = power #0-100
        self.age = age #years
        self.weight = weight #kg


class Car:
    producer = "Renault"

    def __init__(self, max_speed, age, weight, model = "Logan"):
        self.max_speed = max_speed #km/h
        self.age = age #years
        self.weight = weight #kg
        self.model = model