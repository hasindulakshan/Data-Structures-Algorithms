class Node:
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None # Right child
        self.value = key  # Node value

class BST:
    def __init__(self):
        self.root = None  # Initialize the root of the BST

    def insert(self, key):
        # Insert a new node with the given key
        if self.root is None:
            self.root = Node(key)  # If tree is empty, set root
        else:
            self._insert(self.root, key)  # Call helper to insert

    def _insert(self, root, key):
        # Helper method to insert a new node recursively
        if key < root.value:
            if root.left is None:
                root.left = Node(key)  # Insert new node as left child
            else:
                self._insert(root.left, key)  # Recurse left
        else:
            if root.right is None:
                root.right = Node(key)  # Insert new node as right child
            else:
                self._insert(root.right, key)  # Recurse right

    def search(self, key):
        # Search for a node with the given key
        return self._search(self.root, key)

    def _search(self, root, key):
        # Helper method to search recursively
        if root is None or root.value == key:
            return root  # Found the node or reached end (None)
        if key < root.value:
            return self._search(root.left, key)  # Search left subtree
        return self._search(root.right, key)  # Search right subtree

    def inorder(self):
        # Inorder traversal: left -> root -> right
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        # Helper method for inorder traversal
        if root:
            self._inorder(root.left, result)  # Visit left subtree
            result.append(root.value)  # Visit root
            self._inorder(root.right, result)  # Visit right subtree

    def delete(self, key):
        # Delete a node with the given key
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        # Helper method to delete a node recursively
        if root is None:
            return root  # Base case: empty tree
        if key < root.value:
            root.left = self._delete(root.left, key)  # Recurse left
        elif key > root.value:
            root.right = self._delete(root.right, key)  # Recurse right
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: get the inorder successor (smallest in the right subtree)
            min_val = self._min_value_node(root.right)
            root.value = min_val.value
            root.right = self._delete(root.right, min_val.value)  # Delete the inorder successor
        return root

    def _min_value_node(self, node):
        # Helper method to find the node with the minimum value (leftmost leaf)
        current = node
        while current.left is not None:
            current = current.left
        return current

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder())  # Output: [20, 30, 40, 50, 60, 70, 80]

bst.delete(20)
print("Inorder after deleting 20:", bst.inorder())  # Output: [30, 40, 50, 60, 70, 80]

found_node = bst.search(40)
if found_node:
    print(f"Node with key 40 found: {found_node.value}")  # Output: Node with key 40 found: 40
else:
    print("Node with key 40 not found")
