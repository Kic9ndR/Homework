def func_sum(*args):
    def total(elements):
        result = []
        for i in elements:
            if isinstance(i, int):
                result.append(i)
            else:
                result.extend(total(i))
        return result
    return sum(total(args))

# summ = ([[1, 2, [3]], [1], 3])
# print('Сумма:', func_sum(summ))
# summ = (1, 2, 3, 4, 5)
# print('Сумма:', func_sum(summ))
