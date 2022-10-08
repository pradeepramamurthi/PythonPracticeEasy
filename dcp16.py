"""You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
>>> get_last(4)
[6, 7, 8, 10]
"""
log = []


def record(order_id):
    log.append(order_id)


def get_last(i):
    try:
        return log[-i:]
    except IndexError:
        print("log has only " + len(log) + " elements , get_last should be called with a parameter <= len(log)")


if __name__ == "__main__":
    record(4)
    record(5)
    record(2)
    record(6)
    record(7)
    record(8)
    record(10)
    print(get_last(4))

    import doctest

    doctest.testmod()
