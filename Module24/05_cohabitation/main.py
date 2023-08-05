from dataclasses import dataclass
from random import randint

@dataclass
class House:
    food: int = 50
    money: int = 0

    def buy_phone(self):
        self.money -= 85

    def spoiled_food(self):
        self.food -= 30


@dataclass
class Human:
    name: str
    house: House
    satiety: int = 50
    
    def eat(self):
        self.satiety += 25 
        self.house.food -= 25

    def work(self):
        self.satiety -= 45
        self.house.money += 50

    def buy_food(self):
        self.house.food += 50
        self.house.money -= 50

    def play(self):
        self.satiety -= 50

    def is_alive(self) -> bool:
        return self.satiety >= 0

    def action(self):
        if not self.is_alive:
            raise ValueError(f'{self.name} умер!')
        dice = randint(1, 6)
        if self.satiety < 20:
            return self.eat()
        elif self.house.food < 10:
            return self.buy_food()
        elif self.house.money < 50:
            return self.work()
        elif dice == 1:
            return self.work()
        elif dice == 2:
            return self.eat()
        else:
            return self.play()


house = House()
person = Human('Сергей', house)
person2 = Human('Кристина', house)

for _ in range(365):
    person.action()
    person2.action()
else:
    print(f'{person.name} и {person2.name} выжили!')