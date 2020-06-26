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
            #if it is a leaf Node
            if (currNode.right is None and currNode.left is None):
                if (parentNode is None):
                    return None
                elif (parentNode.value < currNode.value):
                    parentNode.right = currNode
                    break
            #if right node is null
            elif (currNode.right is None):
                #remove root node case
                if (parentNode is None):
                    root = currNode.left
                else:
                    #if not root Node
                    #node to remove is found at the left side
                    if (parentNode.value > currNode.value):
                        parentNode.left = currNode.left
                    elif (parentNode.value < currNode.value):
                        parentNode.right = currNode.left




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
