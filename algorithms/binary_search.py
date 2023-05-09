from random import randint


def binary_search(row: list, goal: int) -> (int, int):
    """defining boundaries in a pre-sorted list"""

    # left border search
    left = 0
    right = len(row)
    while right - left > 1:
        middle = (left + right) // 2
        if row[middle] < goal:
            left = middle
        else:
            right = middle
    left_bound = left

    # right border search
    left = 0
    right = len(row)
    while right - left > 1:
        middle = (left + right) // 2
        if row[middle] > goal:
            right = middle
        else:
            left = middle

    # edge adjustment
    if goal < row[0]:
        right = 0
    if goal > row[-1]:
        left_bound = len(row)
    if left_bound >= len(row):
        left_bound = len(row) - 1
    if right >= len(row):
        right = len(row) - 1

    return left_bound, right


def binary_search_demonstration(goal: int):
    row = [0] * 30
    for i in range(30):
        row[i] = randint(1, 9) * 10

    row.sort()

    left_bound, right_bound = binary_search(row, goal)

    result = [""] * 30
    for i in range(left_bound, right_bound + 1):
        if i < len(row):
            result[i] = 88

    print(
        " demonstration of the binary search function - search for ", goal,
        "- founded external boundaries ", left_bound, right_bound,
        "\n",
        row,
        "\n",
        result,
        "\n"
    )


if __name__ == '__main__':
    binary_search_demonstration(9)

    for i in range(3):
        binary_search_demonstration(
            randint(3, 8) * 10
        )

    binary_search_demonstration(100)
