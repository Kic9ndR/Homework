from collections.abc import Iterable

def flatten(items: Iterable):
    for item in items:
        if isinstance(item, Iterable):
            yield from flatten(item)
        else:
            yield item

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', list(flatten(nice_list)))