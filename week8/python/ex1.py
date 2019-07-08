print('for loop')
for i in range(1, 41):
    print(i)

print('while loop')
i = 1
while i <= 40:
    print(i)
    i += 1

print('3:')
for i in range(1, 101):
    if (i % 3) == 0:
        print('Fizz')
    elif (i % 5) == 0:
        print('Buzz')
    elif (i % 3) & (i % 5) == 0:
        print('FizzBuzz')
    else:
        print(i)
