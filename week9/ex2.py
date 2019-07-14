def find_max(list,index):
    if index == len(list):
       return 0
    nextItem = find_max(list, index + 1)
    return nextItem if nextItem > list[index] else list[index]

assert(find_max([1, 2, 3], 0) == 3)
assert(find_max([100, 2, 100], 0) == 100)
assert(find_max([], 0) == 0) # what is your return value for empty list?
assert(find_max([11], 0) == 11)
assert(find_max([11, 0], 0) == 11)
assert(find_max([11, -19], 0) == 11)
