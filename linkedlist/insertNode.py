class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    #self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    #self.tail = None

  def insertNode(self, value):
    newNode = Node(value)

    if self.head is None:
      self.head = newNode
    else:
      temp = self.head;
      while (temp.next):
        temp = temp.next
      temp.next = newNode

  def mergedList(self, ll1, ll2):
    if ll1 is None:
      return ll2
    if ll2 is None:
      return ll1

    if ll1.value < ll2.value:
      self.head = ll1
      ll1 = ll1.next
    else:
      self.head = ll2
      ll2 - ll2.next


  def printlist(self):
    temp = self.head
    while (temp):
      print(temp.value)
      temp = temp.next

ll1 = LinkedList()
ll2 = LinkedList()

ll1.insertNode(5)
ll1.insertNode(7)
ll1.insertNode(9)
ll1.insertNode(11)

ll2.insertNode(6)
ll2.insertNode(8)
ll2.insertNode(10)
ll2.insertNode(12)
ll2.insertNode(14)
ll2.insertNode(16)

ll1.printlist()
print('\n')
ll2.printlist()

ml = LinkedList()
ml.mergedList(ll1, ll2)
