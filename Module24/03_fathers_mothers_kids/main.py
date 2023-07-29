class Kid():

    def __init__(self, name: str, age: int, status_calm: bool, status_hunger: bool) -> None:
        #True - Беспокоится или голодный, False - Не беспокоится или не голодный
        self.name = name
        self.age = age      #Должен быть младше минимум на 16 лет
        self.status_calm = status_calm
        self.status_hunger = status_hunger

class Parent():

    def __init__(self, name: str, age: int, list_kids: list) -> None:
        self.name = name
        self.age = age
        self.list_kids = list_kids

    def __str__(self) -> str:       #Информация о родителе
        return f'Меня зовут {self.name}, у меня {len(self.list_kids)} детей и мне {self.age} лет'
    
    def feed_baby(self):
        for name, age, hunger, calm in self.list_kids:
            if hunger == True:
                print(f'{name} ребенок голоден, сейчас покормлю его.')
                hunger = False
            else:
                print("Ребенок не хочет кушать.")
        return hunger

    def calm_child(self):
        for name, age, hunger, calm in self.list_kids:
            if calm == True:
                print(f'{name} беспокоится, сейчас я его успокою')
            else:
                print('Ребенок не беспокоится.')
        return calm
    

Sofi = Kid("sofi", 10, True, False)
Bob = Kid('Bob', 6, False, True)
Alex = Kid('Alex', 2, True, True)

kids = [Sofi, Bob, Alex]

mom = Parent('Kate', 30, kids)

print(mom)
mom.calm_child()
mom.feed_baby()