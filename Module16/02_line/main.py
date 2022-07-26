class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 3))

class_1.extend(class_2)

for i_cur in range(len(class_1) - 1):
    for i in range(len(class_1) - 1):
        if class_1[i] > class_1[i + 1]:
            class_1[i], class_1[i + 1] = class_1[i + 1], class_1[i]

print('Отсортированный список учеников:', class_1)