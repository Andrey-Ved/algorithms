class HashTable:
    def __init__(self, size):
        assert size > 10, "expected that table size would be greater than 10"
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def put(self, index, data):
        hash_value = self.hash_function(index, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = index
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == index:
                self.data[hash_value] = data
            else:
                next_slot = self.rehash(hash_value, len(self.slots))

                while self.slots[next_slot] is not None and self.slots[next_slot] != index:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = index
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def find_slots(self, index):
        start_slot = self.hash_function(index, len(self.slots))
        slot = start_slot

        while self.slots[slot] is not None:
            if self.slots[slot] == index:
                return slot
            else:
                slot = self.rehash(slot, len(self.slots))
                if slot == start_slot:
                    return slot

        return slot

    def get(self, index, extract=False):
        slot = self.find_slots(index)

        if self.slots[slot] != index:
            return None

        data = self.data[slot]

        if extract:
            self.data[slot] = None
            self.slots[slot] = 0

        return data

    def extract(self, index):
        return self.get(index, extract=True)

    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, data):
        self.put(index, data)

    def fullness(self):
        number_of_used = 0
        for item in self.slots:
            number_of_used += 1 if item is not None else 0

        return number_of_used / len(self.slots)


def hash_table_demonstration():
    primer = ["Иванов",
              "Петров",
              "Сидоров",
              "Маврыкин",
              "Белов",
              "Гладкий",
              "Чикатило",
              "Ленин",
              "Сталин"]

    test_hash_table = HashTable(11)

    for index, data in enumerate(primer):
        test_hash_table[index * 10 + 5] = data

    print()

    for index, data in enumerate(test_hash_table.data):
        print(test_hash_table.slots[index], "-", data)

    print()
    item = 90
    print("пробуем удалить несуществующий элемент", item, "-", test_hash_table.extract(item))
    item = 75
    print("удаляемменяем значение", item, "-", test_hash_table.extract(item))
    item = 90
    print("пробуем получить несуществующий элемент", item, "-", test_hash_table[item])
    item = 85
    test_hash_table[item] = 'Ельцин'
    print("меняем значение у", item, "на", test_hash_table[item], "\n")

    for index, data in enumerate(test_hash_table.data):
        print(test_hash_table.slots[index], "-", data)

    print()
    print("текущая заполненность таблицы {:.2f}".format(test_hash_table.fullness()))


if __name__ == '__main__':
    hash_table_demonstration()
