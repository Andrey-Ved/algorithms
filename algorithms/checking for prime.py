from random import randint


def is_prime(n):
    assert isinstance(n, int), 'integer expected'

    if n % 2 == 0:
        return n == 2

    d = 3

    while d * d <= n and n % d != 0:
        d += 2

    return d * d > n


def is_prime_demonstration():
    for i in range(10):
        n = randint(1, 100)

        print(n, end=' - ')
        print(["it's a composite number", "it's a prime number"][is_prime(n)])


if __name__ == '__main__':
    is_prime_demonstration()
