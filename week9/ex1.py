def sum(list, index):
    if index == len(list):
        return 0
    return sum(list, index + 1) + list[index]


assert(sum([1, 2, 3, 4, 5], 0) == 15)
assert(sum([], 0) == 0)
assert(sum([11], 0) == 11)
assert(sum([11, 0], 0) == 11)
assert(sum([11, -1], 0) == 10)
