# in the singly linked list, each nod contains a data and reference to the next node in the list. Traversal is one-directional, starting from the head node.

# ========================================================================================================
# Implementing a singly linked list in Python
# ========================================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion Methods
    
    # 01. Insert at the beginning
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
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
    
    # 03. Insert at a specific position (0th index based)
    def insertAtPosition(self, position, data):
        if position == 0:
            self.insertAtPosition(data)
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
    
    # Delete Methods
    
    # 01. Delete the first node
    def deleteFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    # 02. Delete the last node
    def deleteLastNode(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    # 03. Delete a node at a specific position
    def deleteAtPosition(self, position):
        if self.head is None:
            print("The list is empty")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        index = 0
        while current is not None and index < position - 1:
            current = current.next
            index += 1
        if current is None or current.next is None:
            print("The Position is out of range")
            return
        current.next = current.next.next
    
    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
# usage of the singly linked list
singly_linked_list = SinglyLinkedList()
singly_linked_list.insertAtBeginning(10)
singly_linked_list.insertAtEnd(20)
singly_linked_list.insertAtPosition(1, 15) # List: 10 -> 15 -> 20
singly_linked_list.display() # Output: 10 -> 15 -> 20 -> None

singly_linked_list.updateNode(1, 25)
singly_linked_list.display()

singly_linked_list.deleteFirstNode()
singly_linked_list.display() # Output: 15 -> 20 -> None

singly_linked_list.deleteLastNode()
singly_linked_list.display() # Output: 15 -> None

singly_linked_list.insertAtEnd(30)
singly_linked_list.insertAtEnd(40)
singly_linked_list.insertAtEnd(50)
singly_linked_list.display()

singly_linked_list.deleteAtPosition(1)
singly_linked_list.display() # Output: 15 -> 40 -> 50 -> None



