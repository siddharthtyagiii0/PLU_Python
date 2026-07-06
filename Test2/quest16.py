
'''
.Find and display all the leaf nodes of a binary tree
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)


def leaf_nodes(current):
    if current:
        if current.left is None and current.right is None:
            print(current.data)

        leaf_nodes(current.left)
        leaf_nodes(current.right)


print("Leaf Nodes are:")
leaf_nodes(root)