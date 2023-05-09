def invert_part_of_list(l: list, a: int, b: int):
    """
        инвертирует часть списка

        :param l:ссылка на список
        :param a:индекс начала фрагмента
        :param b:индекс окончания фрагмента
    """
    assert a >= 0, "expected was index to be positive"
    assert a < b, "expected was second index to be greater than first"
    assert b < len(l), "expected was index to be within list length"

    for i in range((b - a) // 2):
        l[a + i], l[b - i] = l[b - i], l[a + i]
    return


def invert_part_of_list_demonstration():
    array = [0] * 50

    for i in range(0, 50):
        array[i] = i

    print(array)

    for i in range(0, 50, 10):
        invert_part_of_list(array, 2 + i, 8 + i)

        print(array)


if __name__ == '__main__':
    invert_part_of_list_demonstration()
