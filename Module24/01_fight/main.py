import random

class Warrior():
    def __init__(self, name: str, health: int = 100, power: int = 20):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other: "Warrior") -> bool:
        print(f'{self.name} атаковал {other.name}!')
        return other.damage(self.power)

    def __str__(self):
        return f'Игрок: {self.name} | Здоровье: {self.health}'

    def damage(self, power: int = 20) -> bool:
        self.health -= power
        is_dead = self.health <= 0

        if not is_dead:
            print(f'У {self.name} осталось {self.health} ХП!\n')
        else:
            print(f'{self.name} умер!')

        return is_dead


war1 = Warrior(name="Воин 1")
war2 = Warrior(name='Воин 2')

while war1.health > 0 and war2.health > 0:
    turn = random.randint(0, 1)
    if turn == 0:
        war1.attack(war2)
    else:
        war2.attack(war1)
