from random import randint


def search_length_lcs(a: str, b: str) -> int:
    """
        поиск наибольшей общей подпоследовательности

        (подпоследовательностью строки называется
        некоторое подмножество символов этой строки,
        следующих в том же порядке, но не обязательно все)

        :param a:первая строка
        :param b:вторая строка
        :return: длинна наибольшей общей подпоследовательности
    """
    solutions_table = [[0] * (len(b)+1) for i in range(len(a)+1)]

    for i in range(0, len(a)):
        for k in range(0, len(b)):
            if a[i] == b[k]:
                solutions_table[i+1][k+1] = solutions_table[i][k] + 1
            else:
                solutions_table[i+1][k+1] = max(
                    solutions_table[i+1][k],
                    solutions_table[i][k+1]
                )

    return solutions_table[-1][-1]


def search_length_lcs_demonstration():
    first_str = ""
    second_str = ""

    for i in range(0, 200):
        first_str += str(randint(0, 9))

    for i in range(0, 200):
        second_str += str(randint(0, 9))

    print(first_str)
    print(second_str)
    print(
        "длинна наибольшей общей подпоследовательности -",
        search_length_lcs(first_str, second_str)
    )
    print()


if __name__ == '__main__':
    for i in range(5):
        search_length_lcs_demonstration()
