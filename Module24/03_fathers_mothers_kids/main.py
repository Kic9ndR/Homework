class Kid():

    def __init__(self, name: str, age: int, status_calm: bool, status_hunger: bool) -> None:
        #True - Беспокоится или голодный, False - Не беспокоится или не голодный
        self.name = name
        self.age = age      #Должен быть младше минимум на 16 лет
        self.status_calm = status_calm
        self.status_hunger = status_hunger
    
    def __str__(self) -> str:
        state_calm = ('спокоен' if self.status_calm == False else 'раздражен')
        state_hunger = ('не голоден' if self.status_hunger == False else 'голоден')
        return f'{self.name} {self.age} лет, он(а) {state_calm} и {state_hunger}'

class Parent():

    childrens = []

    def __init__(self, name: str, age: int, list_kids: list) -> None:
        self.name = name
        self.age = age
        for kid in list_kids:
            if age - kid.age > 16:
                self.childrens.append(kid)
            else:
                print(f'\n{kid.name} не ваш ребенок!\n')

    def __str__(self) -> str:       #Информация о родителе
        return f'Меня зовут {self.name}, у меня {len(self.childrens)} детей и мне {self.age} лет\n'
    
    def feed_baby(self):
        for hunger in self.childrens:
            if hunger.status_hunger == True:
                print(f'Надо покормить {hunger.name}')
                hunger.status_hunger = False
            else:
                print(f'{hunger.name} не голоден')


    def calm_child(self):
        for calm in self.childrens:
            if calm.status_calm == True:
                print(f'Надо поиграть с {calm.name}, чтобы он успокоился')
                calm.status_calm = False
            else:
                print(f'{calm.name} спокоен')
    

Sofi = Kid("Sofi", 10, True, False)
Bob = Kid('Bob', 6, False, True)
Alex = Kid('Alex', 5, True, True)

mom = Parent('Kate', 30, [Sofi, Bob, Alex])

print(mom)
print('{}\n{}\n{}'.format(
    Sofi, Bob, Alex
))
mom.calm_child()
mom.feed_baby()
print('{}\n{}\n{}'.format(
    Sofi, Bob, Alex
))