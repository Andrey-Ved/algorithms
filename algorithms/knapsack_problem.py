from random import randint


def choosing_things(knapsack_size: int, things_size: list, things_cost: list) -> int:
    """
        определение максимума возможной общей стоимости
        предметов входящих в рюкзак ограниченного размера
    """

    assert len(things_size) == len(things_cost), "expected was lists to have the same length"

    solutions_table = [
        [0] * (len(things_cost)+1)
        for _ in range(knapsack_size+1)
    ]

    for k in range(1, knapsack_size+1):
        for i in range(1, len(things_cost)+1):
            if things_size[i-1] <= k:
                solutions_table[k][i] = max(
                    solutions_table[k][i-1],
                    things_cost[i-1] + solutions_table[k - things_size[i-1]][i-1]
                )
            else:
                solutions_table[k][i] = solutions_table[k][i-1]

    return solutions_table[knapsack_size][len(things_cost)]


def choosing_things_demonstration(items_number=5):

    knapsack_size = randint(8, 10)
    things_size = [randint(1, 8) for _ in range(items_number)]
    things_cost = [randint(2, 9) for _ in range(items_number)]

    print()
    print("размер рюкзака -----", knapsack_size)
    print("размер предмета ----", *things_size)
    print("цена предмета ------", *things_cost)
    print("максимум стоимости -", choosing_things(knapsack_size, things_size, things_cost))


if __name__ == '__main__':
    for i in range(3):
        choosing_things_demonstration()
