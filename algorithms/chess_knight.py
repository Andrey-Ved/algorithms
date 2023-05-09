from _collections import deque


def finding_path(start_vertex, finish_vertex):
    # graph formation
    letters = "abcdefgh"
    numbers = "12345678"

    graph = {}
    for letter in letters:
        for number in numbers:
            graph[letter + number] = set()

    def add_edge(vertex_1, vertex_2):
        graph[vertex_1].add(vertex_2)
        graph[vertex_2].add(vertex_1)

    for letter in range(len(letters)):
        for n in range(len(numbers)):
            vertex_1 = letters[letter] + numbers[n]

            if 0 <= letter + 2 < len(letters) and 0 <= n + 1 < len(numbers):
                vertex_2 = letters[letter + 2] + numbers[n + 1]
                add_edge(vertex_1, vertex_2)

            if 0 <= letter - 2 < len(letters) and 0 <= n + 1 < len(numbers):
                vertex_2 = letters[letter - 2] + numbers[n + 1]
                add_edge(vertex_1, vertex_2)

            if 0 <= letter + 1 < len(letters) and 0 <= n + 2 < len(numbers):
                vertex_2 = letters[letter + 1] + numbers[n + 2]
                add_edge(vertex_1, vertex_2)

            if 0 <= letter - 1 < len(letters) and 0 <= n + 2 < len(numbers):
                vertex_2 = letters[letter - 1] + numbers[n + 2]
                add_edge(vertex_1, vertex_2)

    # Breadth First Search
    distances = {v: None for v in graph}
    parents = {v: None for v in graph}

    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        cur_v = queue.popleft()

        for neigh_v in graph[cur_v]:
            if distances[neigh_v] is None:
                distances[neigh_v] = distances[cur_v] + 1
                parents[neigh_v] = cur_v
                queue.append(neigh_v)

    path = [finish_vertex]
    parent = parents[finish_vertex]

    while parent is not None:
        path.append(parent)
        parent = parents[parent]

    return path[::-1]


def finding_path_demonstration():
    start_vertex = "a4"
    finish_vertex = "f7"

    print("\n шахматный коь стартует с клетки -", start_vertex,
          "\n задача - найти кротчайший путь до клетки -", finish_vertex)

    path = finding_path(
        start_vertex="a4",
        finish_vertex="f7"
    )

    print("\n искомый путь -", *path)


if __name__ == '__main__':
    finding_path_demonstration()
