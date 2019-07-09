def sumOfList(list):
    for element in list:
        if(type(element) != int):
            return 'false'

    return sum(list)


res = sumOfList([2, 3, 4, 1, 2, 3, 4,'dfdf'])
print(res)
