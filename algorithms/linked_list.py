from random import randint


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_item(self, item):
        if not isinstance(item, ListNode):
            node = ListNode(item)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def length(self):
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def output_list(self):
        node = self.head
        out = []

        while node is not None:
            out.append(node.data)
            node = node.next

        return out

    def remove_item_by_id(self, item_id):
        current_id = 0
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return

            previous_node = current_node
            current_node = current_node.next
            current_id += 1

    def revers(self):
        previous_node = self.head

        if previous_node is None or previous_node.next is None:
            return

        current_node = previous_node.next
        previous_node.next = None

        while current_node.next is not None:
            (
                current_node.next,
                current_node,
                previous_node
            ) = (
                previous_node,
                current_node.next,
                current_node
            )

        current_node.next = previous_node
        self.head = current_node

    def __getitem__(self, item_id):
        assert 0 <= item_id < self.length(), "index was expected to be within list"

        current_id = 0
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                return current_node.data

            current_node = current_node.next
            current_id += 1

    def __setitem__(self, item_id, data):
        assert 0 <= item_id < self.length(), "index was expected to be within list"

        current_id = 0
        current_node = self.head

        while current_node is not None:
            if current_id == item_id:
                current_node.data = data
                return

            current_node = current_node.next
            current_id += 1


def linked_list_demonstration():
    original = [i for i in range(10, 31)]
    print(
        original,
        "- образец данных, поэлементно добавляем в конец связанного списка"
    )

    test_list = LinkedList()

    for item in original:
        test_list.add_item(item)

    print(
        test_list.output_list(),
        "- считано из связанного списка"
    )
    print(
        "количество элементов в связанном списке: ",
        test_list.length()
    )

    for n in [
        0,
        randint(1, test_list.length() - 2),
        test_list.length() - 3,
        test_list.length() + 100
    ]:
        test_list.remove_item_by_id(n)

        print(
            test_list.output_list(),
            "- удалён %i элемент" % n
        )

    print(
        "количество элементов в связанном списке:",
        test_list.length()
    )

    n = randint(1, test_list.length())

    print(
        "считывание (случайно выбранного) %i элемента - " % n,
        test_list[n]
    )

    test_list[n] = test_list[n] // 2

    print(
        test_list.output_list(),
        "- состояние списка после деления %i элемента пополам" % n
    )

    test_list.revers()

    print(
        test_list.output_list(),
        "- состояние списка после реверса очерёдности элементов"
    )


if __name__ == '__main__':
    linked_list_demonstration()
