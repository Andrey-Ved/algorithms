from math import gcd as math_gcd
from random import randint


def find_gcd_dev(a: int, b: int) -> int:
    """finding the greatest common divisor by division"""
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def find_gcd_sub(a: int, b: int) -> int:
    """finding the greatest common divisor by subtraction"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def test_find_gcd(tested_func, attempts_number=10**4):
    test_result = 'passed'

    for i in range(attempts_number):
        x, y = randint(1, 100), randint(1, 1000)

        if math_gcd(x, y) != tested_func(x, y):
            test_result = 'failed'
            break

    print(f'{tested_func.__name__} function test - {test_result}')

    return True if test_result == 'passed' else False

if __name__ == '__main__':
    test_find_gcd(find_gcd_sub)
    test_find_gcd(find_gcd_dev)
