def merge(a: list, b: list) -> list:
    c = a[:] + b[:]
    i, k, n = 0, 0, 0

    while i < len(a) and k < len(b):
        if a[i] < b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1

    return c[:n] + a[i:] + b[k:]


def merge_sort(a: list) -> list:
    if len(a) <= 1:
        return a

    middle = len(a) // 2
    return merge(merge_sort(a[:middle]), merge_sort(a[middle:]))


def hoar_sort(a: list) -> list:
    """sorting by Tony Hoare (with primitive choice of barrier element)"""

    if len(a) <= 1:
        return a

    barrier = a[0]
    left, middle, right = [], [], []

    for x in a:
        if x < barrier:
            left.append(x)
        elif x > barrier:
            right.append(x)
        else:
            middle.append(x)

    return hoar_sort(left) + middle + hoar_sort(right)


def sort_demonstration(function_name):
    print("\n", function_name.__name__)

    first = [0] * 30
    for i in range(15):
        first[15+i] = 29 - i
        first[i] = 14 - i

    second = function_name(first)
    third = first[:]

    for i in range(30):
        third[i] = i

    print(
        "",
        first, "\n",
        second, "\n",
        third, "\n",
        second == third
    )


if __name__ == '__main__':
    sort_demonstration(merge_sort)
    sort_demonstration(hoar_sort)
