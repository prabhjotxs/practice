import timeit

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

def finditem(root, value):
    if root is None:
        return False

    conditions = 0
    curNode = root
    while(True):
        conditions = conditions + 1

        if (curNode.value == value):
            print(conditions)
            return True

        if (curNode.value < value):
            if (curNode.right is not None):
                curNode = curNode.right
            else:
                print("\n", value)
                break
        else:
            if (curNode.left is not None):
                curNode = curNode.left
            else:
                print("\n", value)
                break

    print(conditions)
    return False


root = Node(40)
insert(root, Node(50))
insert(root, Node(30))
insert(root, Node(20))
insert(root, Node(35))
insert(root, Node(45))
insert(root, Node(42))
insert(root, Node(41))

printtree(root)

t0 = timeit.timeit()
if (True == finditem(root, 43)):
    print("Found!")
else:
    print("Not found!")
t1 = timeit.timeit()

print(t1-t0)
