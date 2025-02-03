# In the doubly linked list, each node as 2 pointers. one pointing to the next node and one pointing to the previous node. can traverse in both directions.

# ========================================================================================================
# Implementation of Doubly Linked List using Python
# ========================================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion Methods

    # 01. Insert at the beginning
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    # 02. Insert at the end
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        newNode.prev = current

    # 03. Insert at a specific position (0th index based)
    def insertAtPosition(self, position, data):
        if position == 0:
            self.insertAtBeginning(data)
            return
        newNode = Node(data)
        current = self.head
        index = 0
        while current is not None and index < position - 1:
            current = current.next
            index += 1
        if current is None:
            print("The Position is out of range")
            return
        newNode.next = current.next
        newNode.prev = current
        if current.next is not None:
            current.next.prev = newNode
        current.next = newNode

    # 04. Update a node at a specific position
    def updateNode(self, position, data):
        current = self.head
        index = 0
        while current is not None and index < position:
            current = current.next
            index += 1
        if current is None:
            print("The Position is out of range")
            return
        current.data = data

    # Deletion Methods

    # 01. Delete the first node
    def deleteFirstNode(self):
        if self.head is None:
            print("The List is empty")
            return
        self.head = self.head.next
        self.head.prev = None

    # 02. Delete the last node
    def deleteLastNode(self):
        if self.head is None:
            print("The List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None

    # 03. Delete a node at a specific position
    def deleteAtPosition(self, position):
        if self.head is None:
            print("The List is empty")
            return
        if position == 0:
            self.removeFirstNode()
            return
        current = self.head
        index = 0
        while current is not None and index < position:
            current = current.next
            index += 1
        if current is None:
            print("The Position is out of range")
            return
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    # Display Method

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Usage


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.insertAtBeginning(10)
doubly_linked_list.insertAtBeginning(5)  # List: 5 <-> 10
doubly_linked_list.insertAtEnd(20)
doubly_linked_list.insertAtPosition(1, 15)  # List: 10 <-> 15 <-> 20
doubly_linked_list.display()  # Output: 10 <-> 15 <-> 20 <-> None

doubly_linked_list.updateNode(1, 25)  # List: 10 <-> 25 <-> 20
doubly_linked_list.display()

doubly_linked_list.deleteFirstNode()  # List: 25 <-> 20
doubly_linked_list.display()

doubly_linked_list.deleteLastNode()  # List: 25
doubly_linked_list.display()

doubly_linked_list.insertAtEnd(30)  # List: 25 <-> 30
doubly_linked_list.insertAtEnd(35)  # List: 25 <-> 30 <-> 35
doubly_linked_list.insertAtEnd(40)  # List: 25 <-> 30 <-> 35 <-> 40
doubly_linked_list.display()

doubly_linked_list.deleteAtPosition(2)  # List: 25 <-> 30 <-> 40
doubly_linked_list.display()  # Output: 25 <-> 30 <-> 40 <-> None
