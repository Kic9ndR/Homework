class Student():

    def __init__(self, full_name: str, class_num: int, grade: tuple) -> None:
        self.full_name = full_name
        self.class_num = class_num
        self.grade = grade
        
    def give_average(self) -> float:
        return round(sum(self.grade) / len(self.grade), 2)
    
    def __str__(self) -> str:
        print()
        return f'Полное имя: {self.full_name}\n№ группы: {self.class_num}\nОценка: {self.give_average()}'


def receiving_data():
    name = input('Введите полное имя: ')
    group = int(input('Введите номер группы: '))
    progress = tuple(map(int, input('Введите оценки (через пробел): ').split()))
    print()
    return name, group, progress


list_student = [Student(*receiving_data()) for _ in range(10)]
print("Наши студенты:")
for stud in list_student:
    print(stud)
print()


list_student.sort(key=lambda x: x.give_average())
print("Отсортированный список студентов:")
for student in list_student:
    print(student)
