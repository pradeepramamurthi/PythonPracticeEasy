"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
>>> checkAddup([10, 15, 3, 7], 17)
True
"""


def checkAddup(inputList, k):
    for x in inputList:

        if (k - x) in inputList:
            return True
            break

    return False


if __name__ == "__main__":
    testList = checkAddup([10, 15, 20, 10, 1, 7], 27)
    print(testList)
    import doctest
    doctest.testmod()
