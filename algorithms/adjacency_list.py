class AdjacencyList:
    def __init__(self, input_edges):
        self.edges_quantity = len(input_edges)
        self.edges = input_edges

        vertices = set()

        for edge in self.edges:
            for vertex in edge:
                vertices.add(vertex)

        self.vertices_quantity = len(vertices)
        self.vertices_name = list(vertices)

        self.vertices_index = {
            self.vertices_name[i]: i
            for i in range(self.vertices_quantity)
        }

        self.adjacency_list = []
        self.vertices_address = [0] * self.vertices_quantity

        for v_name in self.vertices_name:
            self.vertices_address[self.vertices_index[v_name]] = len(self.adjacency_list)
            for v1, v2 in self.edges:
                for u1, u2 in ((v1, v2), (v2, v1)):
                    if v_name == u1:
                        self.adjacency_list.append(self.vertices_index[u2])

    def print_list_construction(self):
        for name in self.vertices_name:
            print(name, self.find_adjacencys(name))

    def checking_adjacency(self, v1: str, v2: str) -> bool:
        return True if v2 in self.find_adjacencys(v1) else False

    def find_quantity_adjacencys(self, v):
        return len(self.find_adjacencys(v))

    def find_adjacencys(self, v):
        adjacencys = []
        i = self.vertices_index[v]

        if i + 1 < len(self.vertices_address):
            l = self.vertices_address[i + 1]
        else:
            l = len(self.adjacency_list) + 1

        for k in self.adjacency_list[self.vertices_address[i]:l]:
            adjacencys.append(self.vertices_name[k])

        return adjacencys

    def dfs(self, vertex: str, used=None):
        """Depth-first search"""

        print(" -", vertex, end=" ")

        if used is None:
            used = set()

        used.add(vertex)
        for neighbour in self.find_adjacencys(vertex):
            if neighbour not in used:
                print(neighbour)

                self.dfs(neighbour, used)


def adjacency_matrix_demonstration():
    input_edges = [('Пермь', 'Кунгур'),
                   ('Горназоводск', 'Кунгур'),
                   ('Пермь', 'Чусовой'),
                   ('Чусовой', 'Горназоводск'),
                   ('Пермь', 'Нытва'),
                   ('Нытва', 'Оханск')]

    print("\n", input_edges)

    G = AdjacencyList(input_edges)
    print(
        "\n", "согласно списку связности мы имеем",
        "\n", "количество вершин -", G.vertices_quantity,
              ", количество рёбер -", G.edges_quantity,
        "\n", "названия вершин - ", G.vertices_index,
        "\n", "список адресов - ", G.vertices_address,
        "\n", "список свяей - ", G.adjacency_list,
        "\n"
    )

    for v1, v2 in [
        ("Пермь", "Нытва"),
        ("Горназоводск", "Пермь")
    ]:
        print(" проверка связи -", v1, v2, end=" - ", )
        print(["отутствует", "есть"][G.checking_adjacency(v1, v2)])
        print(" связи у", v1, end=" - ")
        print(G.find_adjacencys(v1))
        print()

    print(" демонстрация обхода графа:")
    G.dfs("Пермь")


if __name__ == '__main__':
    adjacency_matrix_demonstration()
