import random
#class node
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

#insert function
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

#remove function
def remove(root, value):
    if root is None:
        return False

    currNode = root
    parentNode = None

    while (currNode):
        if (currNode.value < value):
            parentNode = currNode
            currNode = currNode.right
        elif (currNode.value > value):
            parentNode = currNode
            currNode = currNode.left
        elif (currNode.value == value):
            #if right node is null
            if (currNode.right is None):
                #remove root node case
                if (parentNode is None):
                    root = currNode.left
                else:
                    if
                parentNode.left = currNode.left




#print tree
def printtree(root):
    if root:
        printtree(root.left)
        print(root.value)
        printtree(root.right)

root = Node(50)
insert(root, Node(75))
for i in range(10):
    insert(root, Node(random.randint(1, 100)))

#print tree
printtree(root)

#remove
remove(root, 75)
