import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_travel_place(self):
        self.travel = Travelling(travel_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.money += self.job.salary
        self.gladness += self.job.gladness
        self.satiety -= 5

    def go_travelling(self):
        self.money -= self.travel.price
        self.gladness += self.travel.gladness

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel...")
            self.money -= 50
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food...")
            self.money -= 20
            self.home.food += 20
        elif manage == "delicacies":
            print("Happy!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.home = 0
        self.gladness -= 5

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today the {day}th day of {self.name}'s life"
        print(f'{day:=^50}', "\n")
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:^50}', "\n")
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = "Home indexes"
        print(f'{"home_indexes":=^50}', "\n")
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = f'{self.car.brand} car indexes'
        print(f'{car_indexes:^50}', "\n")
        print(f'Fuel - {self.car.fuel}')
        print(f'Strength - {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print("Depression...")
            return False
        elif self.satiety <= 0:
            print("Dead...")
            return False
        if self.money <= -100:
            print("Bankrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home == None:
            print("Settled in the home")
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job == None:
            self.get_job()
            print(f"I don't have a job, so I am going to have a job {self.job.job}"
                  f" with salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 17)
        if self.satiety < 20:
            print("Pizza time")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("I need to chill, but there is a mess...")
                self.clean_home()
            else:
                print("Let's chill")
                self.chill()
        elif self.money <= 10:
            print("Start working!")
            self.work()
        elif self.car.strength <= 10:
            print("I need to repair my car...")
            self.to_repair()
        elif dice >= 1 and dice <= 4:
            print("Chill time")
            self.chill()
        elif dice >= 5 and dice <= 8:
            print("Start working")
            self.work()
        elif dice >= 9 and dice <= 12:
            print("Clean home")
            self.clean_home()
        elif dice >= 13 and dice <= 16:
            print("Shopping time")
            self.shopping(manage="delicacies")
        elif dice == 17:
            if self.money <= self.travel.price:
                print("I wanna go travelling, but I")
                print("have not enough money for this...")
                self.work()


class Auto:
    def __init__(self, brand_list):
        print(list(brand_list))
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car cannot move")
            return False


class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness = job_list[self.job]["job_gladness"]


    #Клас, котрий я додав
class Travelling:
    def __init__(self, travel_list):
        self.place = random.choice(list(travel_list))
        self.price = travel_list[self.place]["price"]
        self.gladness = travel_list[self.place]["travel_gladness"]


travel_list = {"Egypt": {"price": 300, "travel_gladness": 45},
               "Turkey": {"price": 250, "travel_gladness": 40},
               "Crimea": {"price": 150, "travel_gladness": 25},
               "Carpathians": {"price": 200, "travel_gladness": 35}}

job_list = {"C++": {"salary": 70, "job_gladness": 5},
            "Python": {"salary": 50, "job_gladness": 10},
            "Java": {"salary": 60, "job_gladness": 8},
            "PHP": {"salary": 40, "job_gladness": 7}}

brands_of_car = {"BMW": {"fuel": 100, "strength": 100, "consumption": 6},
                 "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
                 "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
                 "Renault": {"fuel": 80, "strength": 120, "consumption": 7}}

print(list(brands_of_car))

nick = Human(name = "Nick")
for day in range(1, 8):
    if nick.live(day) == False:
        break