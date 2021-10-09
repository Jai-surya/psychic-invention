class Node:
    """
    An object for storing a single node in a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        returns the number of nodes in the list
        takes O(n) time
        :return: int
        """
        current = self.head
        count = 0
        while current:  # same as while current != None:
            count += 1
            current = current.next_node
        return count


N1 = Node(10)
print(N1)
N2 = Node(32)
print(N2)
N1.next_node = N2
print(N1.next_node)
