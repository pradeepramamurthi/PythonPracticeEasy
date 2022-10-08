"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

>>> list_intersection(ll1.head,ll2.head)
8
"""


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None


def list_intersection(a, b):
    testlist = []

    while a is not None:
        testlist.append(a)
        a = a.next

    while b is not None:
        if b in testlist:
            return b.val
        b = b.next
    return None


if __name__ == "__main__":
    # Create Nodes and link nodes
    n1 = ListNode(3)
    n2 = ListNode(7)
    n3 = ListNode(8)
    n4 = ListNode(10)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    k1 = ListNode(99)
    k2 = ListNode(1)
    k3 = n3  # intersecting node
    k4 = n4

    k1.next = k2
    k2.next = k3
    k3.next = k4

    # Create Linked List and assign head of ll1 & ll2
    ll1 = SLL()
    ll1.head = n1
    ll2 = SLL()
    ll2.head = k1

    print(list_intersection(ll1.head, ll2.head))

    import doctest

    doctest.testmod()
