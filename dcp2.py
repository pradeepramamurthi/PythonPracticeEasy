"""Given an array of integers, return a new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example,
if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
>>> prodExceptIndex2([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]
"""
resultArray = []

# Time Complexity is O(n^2)
def prodExceptIndex(inputList):
    new_arr = []
    for x in range(0, len(inputList)):
        prod = 1
        for y in range(0, len(inputList)):
            if x != y:
                prod = prod * inputList[y]
        new_arr.append(prod)
    return new_arr

# Time Complexity is O(n)
def prodExceptIndex2(inputList):
    new_arr = []
    prod = 1
    for x in inputList:
        prod = prod * x
    for x in inputList:
        new_arr.append(int(prod/x))
    return new_arr


if __name__ == "__main__":
    testList = prodExceptIndex([3, 2, 3, 1])
    print(testList)
    testList2 = prodExceptIndex2([3, 2, 3, 1])
    print(testList2)
    import doctest
    doctest.testmod()
