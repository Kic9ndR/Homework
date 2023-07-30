class Earth():

    earth = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Time):
            return Stone()  

    def __str__(self) -> str:
        return Earth.earth

class Water():

    water = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Time):
            return Drops() 
        elif isinstance(other, Earth):
            return Dirt()

    def __str__(self) -> str:
        return Water.water

class Fire():

    fire = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Time):
            return Spark()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        

    def __str__(self) -> str:
        return Fire.fire

class Air():

    air = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Time):
            return Vacuum()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Earth):
            return Dust()

    def __str__(self) -> str:
        return Air.air

class Time():       #+ водой = капли, + земля = камень, + огонь = искры, + воздух = вакуум
    
    time = "Время"

    def __add__(self, other):
        if isinstance(other, Air):
            return Vacuum()
        elif isinstance(other, Fire):
            return Spark()
        elif isinstance(other, Water):
            return Drops()
        elif isinstance(other, Earth):
            return Stone()  
        
    def __str__(self) -> str:
        return Time.time

class Dirt():
    title = 'Грязь'

    def __str__(self) -> str:
        return Dirt.title

class Lava():
    title = 'Лава'

    def __str__(self) -> str:
        return Lava.title

class Dust():
    title = 'Пыль'

    def __str__(self) -> str:
        return Dust.title

class Lightning():
    title = 'Молния'

    def __str__(self) -> str:
        return Lightning.title

class Shtorm():
    title = 'Шторм'

    def __str__(self) -> str:
        return Shtorm.title

class Steam():
    title = 'Пар'

    def __str__(self) -> str:
        return Steam.title

class Stone():
    title = 'Камень'

    def __str__(self) -> str:
        return Stone.title

class Vacuum():
    title = 'Вакуум'

    def __str__(self) -> str:
        return Vacuum.title

class Drops():
    title = 'Капли'

    def __str__(self) -> str:
        return Drops.title

class Spark():
    title = 'Искры'

    def __str__(self) -> str:
        return Spark.title


earth = Earth()
water = Water()
fire = Fire()
air = Air()
time = Time()

print(f'{water} + {air} = {water + air}')
print(f'{water} + {earth} = {water + earth}')
print(f'{water} + {fire} = {water + fire}')
print(f'{water} + {time} = {water + time}')
print(f'{earth} + {air} = {earth + air}')
print(f'{earth} + {fire} = {earth + fire}')
print(f'{earth} + {time} = {earth + time}')
print(f'{fire} + {air} = {fire + air}')
print(f'{fire} + {time} = {fire + time}')
print(f'{time} + {air} = {time + air}')