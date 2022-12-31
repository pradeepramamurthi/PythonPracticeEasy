"""
Problem:
Given an array of integers, find the first missing positive integer in linear time and
constant space. In other words, find the lowest positive integer that does not exist in
the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

>>> checkMinMissingInteger([3, 4, -1, 1])
2
"""


# Time Complexity O(n)

# First find the length of the Array.
# Find the max positive element in the given array.
# start at 1 (min positive integer) & keep incrementing by 1 while checking it's absence in the given array.
# the first element not to be present in the given array (absent) is the result element
# If all elements from min postive  to max positive are present in the given input array, then the result is (max positive of Given List + 1)

# Time Complexity is O(n)

# Helper function to find maxpostive number in the given array. min is always set to 1.
def getMinMax(inputList):
    minpostive = 1
    maxpostive = inputList[0]
    for i in range(1, len(inputList)):
        if inputList[i] > maxpostive:
            maxpostive = inputList[i]
    return minpostive, maxpostive


def checkMinMissingInteger(inputList):
    min, max = getMinMax(inputList)

    # Case when there are no positive integers in the given array.
    if max < 1:
        return 1

    for x in range(min, max + 1):
        if x not in inputList:
            return x
    return max + 1


if __name__ == "__main__":
    testList = checkMinMissingInteger([1, 2, 0])
    print(testList)

    import doctest
    doctest.testmod()
