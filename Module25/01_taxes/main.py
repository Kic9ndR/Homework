class Property():
    __worth = 0
 
    def __init__(self, worth):
        self.__worth = self.set_worth(worth)
 
    def set_worth(self, worth):
        if worth > 0:
            return worth
        else:
            raise ValueError("Значение должно быть больше нуля")
 
    def get_worth(self):
        return self.__worth
 
    def tax(self):
        return self.__worth
 
 
class Apartment(Property):
    name = "Квартира"
 
    def __init__(self, worth):
        super().__init__(worth)
 
    def tax(self):
        return super().get_worth() / 1000
 
 
class Car(Property):
    name = 'Машина'
 
    def __init__(self, worth):
        super().__init__(worth)
 
    def tax(self):
        return super().get_worth() / 200
 
 
class CountryHouse(Property):
    name = "Дача"
 
    def __init__(self, worth):
        super().__init__(worth)
 
    def tax(self):
        return super().get_worth() / 500
 
print(' ***** Расчет налогов на имущество *****')
sum_nalog = 0
amount_money = int(input('Введите количество имеющихся денег: '))
 
 
wroth_1 = float(input('"Ценник квартиры: '))
wroth_2 = float(input('Ценник машины: '))
wroth_3 = float(input('Ценник дачи:: '))
 
tax_list = [Apartment(wroth_1), Car(wroth_2), CountryHouse(wroth_3)]
 
for elem in tax_list:
    print('Налог на {} составит {}'.format(
        elem.name,
        elem.tax()
    ))
    sum_nalog += elem.tax()
 
print(f"\nСумма налога составила {sum_nalog}")
 
if sum_nalog > amount_money:
    print(f"Вам не хватает, {sum_nalog - amount_money} для расчета с налоговой")
else:
    print(f"У вас получилось, осталось {amount_money - sum_nalog} наличных")