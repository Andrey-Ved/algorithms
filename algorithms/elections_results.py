from random import randint


def counting_results(elections: list) -> dict:
    counting = {}

    for item in elections:
        if item in counting:
            counting[item] += 1
        else:
            counting[item] = 1

    return counting


participants = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth"
]


voters_number = 100
elections = [""] * voters_number

# fake voting results
for i in range(voters_number):
    k = (randint(0, 9) + randint(0, 5)) // 2

    # manipulation of results
    elections[i] = participants[6 if 2 <= k <= 4 else k]

print()
print("voting results:")
print()

results = counting_results(elections)
for key in results:
    print(key, "-", results[key])
