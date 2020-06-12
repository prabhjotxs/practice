class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, node):
    if (root is None):
        root = node
        return

    if (node.value < root.value):
        if (root.left is None):
            root.left = node
        else:
            insert(root.left, node)

    if (node.value >= root.value):
        if (root.right is None):
            root.right = node
        else:
            insert(root.right, node)

def printtree(root):
    if root:
        printtree(root.left)
        print(root.value)
        printtree(root.right)

root = Node(40)
insert(root, Node(50))
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(35))
insert(root, Node(45))
insert(root, Node(42))


printtree(root)
