nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [step_3 for step_1 in nice_list for step_2 in step_1 for step_3 in step_2]
print('Ответ:', new_list)