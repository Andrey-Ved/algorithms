from random import randint


def routes_search(accessibility: list) -> (int, int):
    """ поиск количества всех маршрутов и количества минимальных прыжков за маршрут

        ввод:
            access:list - доступность путевой точки :bool
        вывод:
            route_sum:int - количество возможных маршрутов
            min_jumps:int - минимальное количество прыжков на путь
    """

    n = len(accessibility)
    route = [0, 0, 0, 1] + [0] * (n - 4)
    for i in range(4, n):
        if accessibility[i]:
            route[i] = (route[i - 1] + route[i - 2] + route[i - 3])
        else:
            route[i] = 0

    min_jumps = [0] * n
    for i in range(4, n):
        if not accessibility[i]:
            min_jumps[i] = 99  # задрали вверх счетчики у недостижимых точек
        else:
            if min_jumps[i - 1] <= min_jumps[i - 2] \
                    and min_jumps[i - 1] <= min_jumps[i - 3]:
                min_jumps[i] = min_jumps[i - 1] + 1
            elif min_jumps[i - 2] <= min_jumps[i - 1] \
                    and min_jumps[i - 2] <= min_jumps[i - 3]:
                min_jumps[i] = min_jumps[i - 2] + 1
            else:
                min_jumps[i] = min_jumps[i - 3] + 1

    return route[-1], min_jumps[-1]


def chose_minimum_cost(accessibility: list, price: list) -> (list, int):
    """ определение маршрута с минимальной стоимостю

        ввод:
            access:list - доступность путевой точки :bool
            price:list - стоимость путевой точки :int 0..5
        вывод:
            way:list дешёвый путь без лишних точек :int
            minimum_cost:int - стоимость самого дешевого пути
    """
    n = len(accessibility)
    assert n == len(price), "ожидалось что списки будут иметь одинаковую длинну"

    for i in range(n):
        if not accessibility[i]:
            price[i] = 99

    way = [0] * n
    min_cost = [99, 99, 99, 0] + [0] * (len(accessibility) - 4)

    for i in range(4, len(accessibility)):
        if min_cost[i - 1] <= min_cost[i - 2] \
                and min_cost[i - 1] <= min_cost[i - 3]:
            min_cost[i] = min_cost[i - 1] + price[i]
            way[i] = i - 1
        elif min_cost[i - 2] <= min_cost[i - 1] \
                and min_cost[i - 2] <= min_cost[i - 3]:
            min_cost[i] = min_cost[i - 2] + price[i]
            way[i] = i - 2
        else:
            min_cost[i] = min_cost[i - 3] + price[i]
            way[i] = i - 3

    point = n - 1
    k = 0

    for i in range(n - 1, 3, -1):
        if i == point:
            point = way[i]
            k += 1
        else:
            way[i] = 0

    way.sort()
    way = way[n - k:]
    way.append(n - 1)

    return way, min_cost[-1]


print(
    """
    кузнечик живущий на числовой прямой
    умеет прыгать по путевым точкам только в перёд
    в начале он находиться на 3 путевой точке 
    (нумерация начинается с нуля)
    за раз он может прыгнуть на 1 или 2 или 3 точки
    мы задаём ему список на какие из путевых точек 
    он может прыгать (или не может)
    а также задаем стоиость пребывания на каждой точке 
    """
)

price = [0, 0, 0, 0]
accessibility = [False, False, False, True]

for i in range(4, 13):
    price.append(randint(0, 5))
    accessibility.append(
        bool(
            randint(0, 1) if i % 5 == 4 else 1
        )
    )

print(accessibility)

print("стоимость точек", price, "\n")

print("расчёт:")
route_sum, min_jumps = routes_search(accessibility)

print("количество маршрутов ------", route_sum)
print("минимум прыжков  ----------", min_jumps)

way, minimum_cost = chose_minimum_cost(accessibility, price)
print("самый экономичный путь---- ", way)
print("затраты на него -----------", minimum_cost)
