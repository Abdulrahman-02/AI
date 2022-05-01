from random import randrange

# generate a list of random numbers


def generate_list(min=0, max=10, count=10):
    numList = []
    for i in range(0, count):
        n = randrange(min, max)
        numList.append(n)
    return numList
