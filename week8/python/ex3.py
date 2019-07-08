def digit5(number):
    number = str(number)
    print("You entered the number: " + number)

    print("The sum of the digits is:",end =" ")
    for digit in number:
        print(digit, end =",")  

    sum = 0
    for digit in number:
        sum += int(digit)

    print("The sum of the digits is: " + str(sum))


digit5(12345)
