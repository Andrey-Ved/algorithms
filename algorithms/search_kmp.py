from random import randint


def kmp_search(big_string: str, search_string: str) -> int:
    """
        finding position of substring in string.
        return: first found location or -1 if there is no result
    """
    s = search_string + "#" + big_string

    # prefix function
    prefix_list = [0] * len(s)
    for i in range(1, len(s) - 1):
        k = prefix_list[i - 1]

        while k > 0 and s[i] != s[k]:
            k = prefix_list[k - 1]

        if s[i] == s[k]:
            k += 1

        prefix_list[i] = k

    # Knuth–Morris–Pratt algorithm
    answer = []
    for i in range(1, len(big_string)):
        if prefix_list[len(search_string) + i] == len(search_string):
            answer.append(i - len(search_string))

    if len(answer) > 0:
        return answer[0]

    return -1


def kmp_search_demonstration():
    big_str = ""
    for i in range(0, 200):
        big_str += str(randint(0, 9))

    random_position = randint(20, 180)

    search_str = big_str[random_position:random_position+10]

    print("искомая подстрока", search_str)

    index = (
            "-" * (random_position-1) +
            "|  задано  |" +
            "-" * (200-random_position-11)
    )

    print(index)

    print(big_str)

    search_index = kmp_search(big_str, search_str)

    if search_index > 0:
        index = (
                "-" * (search_index-1) +
                "|  найдено |" +
                "-" * (200-search_index-11)
        )

        print(index)

        print(
            "найденная подстрока - ",
            big_str[search_index:search_index+10]
        )
        print(
            "тест поиска подстроки - ",
            big_str[search_index:search_index+10] == search_str
        )
    else:
        print("подстрока не нашлась, тест поиска подстроки - False")


if __name__ == '__main__':
    for i in range(2):
        kmp_search_demonstration()
        print()
