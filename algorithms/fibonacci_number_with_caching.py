from random import randint


fibonacci_series = {}


def fibonacci_number(n: int) -> int:
    assert 0 <= n <= 1000, "expected that n in the range from 0 to 1000"

    if n not in fibonacci_series:
        if n <= 1:
            fibonacci_series[n] = n
        else:
            fibonacci_series[n] = fibonacci_number(n - 1) + fibonacci_number(n - 2)

    return fibonacci_series[n]


def fibonacci_number_demonstration():
    for i in range(5):
        n = randint(10, 100)
        print(n, "---", fibonacci_number(n))

    print(1000, "-", fibonacci_number(1000))


if __name__ == '__main__':
    fibonacci_number_demonstration()
