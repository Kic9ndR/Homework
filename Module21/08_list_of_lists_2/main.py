def simple_list(lst):
    if not lst:
        return []
    return simple_list(lst[:-1]) + (simple_list(lst[-1]) if not isinstance(lst, list) else simple_list(lst[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', simple_list(nice_list))
