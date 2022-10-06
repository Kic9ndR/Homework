students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def list_ID():
    lst_stud = {}
    for ID, parametrs in students.items():
        for data, info in parametrs.items():
            if data == 'age':
                lst_stud[ID] = info

    return print(f'Список пар "ID студента — возраст": {lst_stud}')


def list_interests():
    all_interests = []
    for ID, parametrs in students.items():
        for data, info in parametrs.items():
            if data == 'interests':
                all_interests += info

    return print(f'Полный список интересов всех студентов: {all_interests}')

def list_surname():
    length_surname = 0
    for ID, parametrs in students.items():
        for data, info in parametrs.items():
            if data == 'surname':
                length_surname += len(info)

    return print(f'Общая длина всех фамилий студентов: {length_surname}')


list_ID()
list_interests()
list_surname()