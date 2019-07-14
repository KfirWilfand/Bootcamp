def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def test_equal(actual, expected, msg=""):
    if actual != expected:
        print('Error testing {}. expected: {}, got {}'.format(msg, expected, actual))


test_equal(fibonacci(0), 0, "fibonacci 0")
test_equal(fibonacci(1), 1, "fibonacci 1")
test_equal(fibonacci(2), 1, "fibonacci 2")
test_equal(fibonacci(3), 2, "fibonacci 3")
test_equal(fibonacci(4), 3, "fibonacci 4")
test_equal(fibonacci(10), 55, "fibonacci 10")
test_equal(fibonacci(17), 1597, "fibonacci 17")
test_equal(fibonacci(33), 3524578, "fibonacci 33")