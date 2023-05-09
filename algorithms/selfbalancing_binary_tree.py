import random


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    @staticmethod
    def checked_height(item):
        return item.height if item else 0

    def balance_factor(self):
        return self.checked_height(self.right) - self.checked_height(self.left)

    def fix_height(self):
        self.height = max(
            self.checked_height(self.right),
            self.checked_height(self.left)
        ) + 1


class BTree:
    def __init__(self):
        self.root = None
        self.size = 0

    @staticmethod
    def rotate_right(item):
        if not item or not item.left:
            return

        left_item = item.left
        (
            item.key,
            left_item.key
        ) = (
            left_item.key,
            item.key
        )
        (
            item.right,
            item.left,
            left_item.left,
            left_item.right
        ) = (
            item.left,
            left_item.left,
            left_item.right,
            item.right
        )
        left_item.fix_height()
        item.fix_height()

    @staticmethod
    def rotate_left(item):
        if not item or not item.right:
            return

        right_item = item.right
        (
            item.key,
            right_item.key
        ) = (
            right_item.key,
            item.key
        )
        (
            item.left,
            item.right,
            right_item.right,
            right_item.left
        ) = (
            item.right,
            right_item.right,
            right_item.left,
            item.left
        )
        right_item.fix_height()
        item.fix_height()

    def balancing(self, item):
        if item.left:
            self.balancing(item.left)

        if item.right:
            self.balancing(item.right)

        if -1 <= item.balance_factor() <= 1:
            return

        elif item.balance_factor() > 2:
            self.rotate_right(item.right)
            self.rotate_left(item)
            return

        elif item.balance_factor() > 1:
            self.rotate_left(item)
            return

        elif item.balance_factor() < -2:
            self.rotate_left(item.left)
            self.rotate_right(item)
            return

        self.rotate_right(item)

    def add(self, key):
        node = TreeNode(key)
        self.size += 1

        if not self.root:
            self.root = node
            return

        self.insert(self.root, node)

    def insert(self, current_root, node):
        if node.key < current_root.key:
            if current_root.left:
                self.insert(current_root.left, node)
            else:
                current_root.left = node
        else:
            if current_root.right:
                self.insert(current_root.right, node)
            else:
                current_root.right = node

        current_root.fix_height()
        self.balancing(current_root)

    def depth(self):
        depth_list = [0] * self.size

        for key in range(self.size):
            if self.root.key == key:
                depth_list[key] = 1
            else:
                next_node = self.root
                current_node = next_node

                while current_node.key != key:
                    depth_list[key] += 1
                    current_node = next_node

                    if key < current_node.key:
                        next_node = current_node.left
                    else:
                        next_node = current_node.right

        return depth_list

    def checking_heights(self):
        height_list = [0] * self.size

        for key in range(self.size):
            if self.root.key == key:
                height_list[key] = self.root.height
            else:
                next_node = self.root
                current_node = next_node

                while current_node.key != key:
                    current_node = next_node
                    height_list[key] = current_node.height

                    if key < current_node.key:
                        next_node = current_node.left
                    else:
                        next_node = current_node.right

        return height_list


def nonrepeating_random(n: int) -> list:
    out_list = [i for i in range(n)]

    for i in range(n - 1, 0, -1):
        k = random.randint(0, i)
        out_list = out_list[0:k] + out_list[k + 1:n] + [out_list[k]]

    return out_list


def symmetrical_filling(depth_list, start, end, k) -> list:
    """creating symmetrically filled list of vertex heights"""

    i = (start + end) // 2
    depth_list[i] = k + 1

    if end - start < 2:
        for i in range(len(depth_list)):
            if depth_list[i] == 0:
                depth_list[i] = k + 2

        return depth_list

    symmetrical_filling(depth_list, start, i - 1, k + 1)
    symmetrical_filling(depth_list, i + 1, end, k + 1)

    return depth_list


def print_tree(key_list, depth_list):
    assert len(key_list) == len(depth_list), "the lists were expected to be the same length"
    print("\n")

    item_size = len(str(max(key_list)))

    for k in range(max(depth_list)):
        for i in range(len(key_list)):
            item = str(key_list[i])
            item = (item_size - len(item)) * " " + item

            print(item if depth_list[i] == k + 1 else " " * item_size, end="  ")

        print()


def binary_tree_demonstration(n=20):
    example = nonrepeating_random(n)

    print(
        "\n",
        "генерируем случайную неповторяющуюся последовательность -",
        example
    )

    depth = [0] * n
    symmetrical_filling(depth, 0, len(depth) - 1, 0)

    print(
        "\n",
        "генерируем симетрично заполненый список высот вершин-",
        depth,
        "\n",
        "выводим нашу последовательность в симметричном варианте высот"
    )

    print_tree(example, depth)

    tree = BTree()

    print(
        "\n создаём дерево и вносим в него нашу последовательность"
    )

    for item in example:
        tree.add(item)

    example.sort()
    print_tree(example, tree.depth())

    print(
        "\n",
        "проверяем высоту поддерева для каждой вершины"
    )

    for height in tree.checking_heights():
        print(height, end="   ")

    print()


if __name__ == '__main__':
    binary_tree_demonstration()
