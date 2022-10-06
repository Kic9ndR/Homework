def slicer(nums_list, final_num):
    tuple_list = []
    amount = {}
    for i_num, nums in enumerate(nums_list):
        if nums == final_num:
            amount[i_num] = nums
    i_slice = tuple(amount)
    if len(i_slice) > 1:
        tuple_list = nums_list[i_slice[0]: i_slice[1] + 1]
        return tuple(tuple_list)
    elif len(i_slice) == 1:
        tuple_list = nums_list[i_slice[0]:]
        return tuple(tuple_list)
    else:
        return tuple(tuple_list)

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))