class AdjacencyMatrix:
    def __init__(self, input_edges):
        self.edges = input_edges
        self.edges_quantity = len(input_edges)

        vertices = set()
        for edge in self.edges:
            for vertice in edge:
                vertices.add(vertice)

        self.vertices_quantity = len(vertices)
        self.vertices = list(vertices)
        self.vertice_index = {
            self.vertices[i]: i
            for i in range(self.vertices_quantity)
        }

        self.matrix = [
            [0] * self.vertices_quantity
            for vertice in self.vertices
        ]

        for v1, v2 in self.edges:
            self.matrix[self.vertice_index[v1]][self.vertice_index[v2]] = 1
            self.matrix[self.vertice_index[v2]][self.vertice_index[v1]] = 1

    def checking_adjacency(self, v1: str, v2: str):
        if v1 in self.vertice_index and v2 in self.vertice_index:
            if v1 not in self.vertice_index or v1 not in self.vertice_index:
                return

            return self.matrix[self.vertice_index[v1]][self.vertice_index[v2]]

    def find_adjacencys(self, v):
        if v in self.vertice_index:
            related = 0

            for i in range(self.vertices_quantity):
                related += self.matrix[self.vertice_index[v]][i]

            return related


def adjacency_matrix_demonstration():
    input_edges = [('Пермь', 'Кунгур'),
                   ('Горназоводск', 'Кунгур'),
                   ('Пермь', 'Чусовой'),
                   ('Чусовой', 'Горназоводск'),
                   ('Пермь', 'Нытва'),
                   ('Нытва', 'Оханск')]

    print(input_edges)

    G = AdjacencyMatrix(input_edges)
    print(
        "\n", "согласно матрице связности мы имеем",
        "\n", "количество вершин -", G.vertices_quantity,
              ", количество рёбер -", G.edges_quantity,
          "\n", "названия вершин - ", G.vertices,
          "\n", "матрица- ", G.matrix)

    for v1, v2 in [
        ("Пермь", "Нытва"),
        ("Пермь", "Горназоводск")
    ]:
        print("\n", "проверка связи -", v1, v2, end=" - ")
        print(["отутствует", "есть"][G.checking_adjacency(v1, v2)])

    for v1 in ["Пермь", "Нытва"]:
        print("\n", "количество связей у", v1, end=" - ")
        print(G.find_adjacencys(v1))


if __name__ == '__main__':
    adjacency_matrix_demonstration()
