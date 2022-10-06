"""A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

the below binary tree has 5 Unival sub trees 4  leaf nodes + (1-1-1) tree
            0
         /     \
        1       0
              /   \
             1     0
           /   \
          1     1

>>> isUnival(root)
False
>>> countUnivals(root)
5
"""

class Node:
    def __init__(self,value):
        self.data = value
        self.leftNode = None
        self.rightNode = None



def isUnival(root):
    if root is None:
        return True
    if (root.leftNode is not None and root.data != root.leftNode.data):
        return False
    if (root.rightNode is not None and root.data != root.rightNode.data):
        return False
    if (isUnival(root.leftNode) and isUnival(root.leftNode)):
        return True

def countUnivals(root):
    if root is None:
        return 0
    total_count = countUnivals(root.leftNode) + countUnivals(root.rightNode)
    if isUnival(root):
        total_count = total_count + 1
    return total_count

if __name__ == "__main__":
    root = Node(0)
    root.leftNode = Node(1)
    root.rightNode = Node(0)
    root.rightNode.leftNode = Node(1)
    root.rightNode.rightNode = Node(0)
    root.rightNode.leftNode.leftNode = Node(1)
    root.rightNode.leftNode.rightNode = Node(1)

    import doctest
    doctest.testmod()

    print("is the Enitre tree a Unival tree: " + str(isUnival(root)))
    print("Count the number of Univals trees in the given tree: " + str(countUnivals(root)))