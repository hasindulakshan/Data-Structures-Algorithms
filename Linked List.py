# Start by creating the Node class

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_front(self, data):
        self.head = Node(data, self.head)

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while (n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end=" => ")
            n = n.next
        print()


s = LinkedList()
s.add_at_front(5)
s.add_at_end(8)
s.add_at_front(9)

s.print_list()
print(s.get_last_node())
