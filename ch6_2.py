import random

elements = [
    "earth",
    "air",
    "fire",
    "water"
]


# print("choice", random.choice(elements))
# taking an element from the list randomly


# print("sample:", random.sample(elements, 2))
# taking two items randomly from the list specified


# print("shuffle:", elements)
# randomize the order of the list


# print("randint:", random.randint(1, 5))
# returning an integer randomly from 1 -5 


# practice example two and three for homework (game of chance)


import random
def main():
    for i in range(3):                   # "i" stands for the iterator
        outcome = spin_wheel()
        print(outcome, end=" ")


def spin_wheel():
    n = random.randint(1, 20)
    # print("Random number generated:", n)
    if n > 15:
        return "Cherries"
    elif n > 10:
        return "Orange"
    elif n > 5:
        return "Plum"
    elif n > 2:
        return "Melon"
    elif n > 1:
        return "Bell"
    else:
        return "Bar"

main()

