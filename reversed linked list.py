class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    #linked list with one element that is head
class LinkedList:
    def __init__(self):
        self.head = None

    # insert element in the linked list
    def insert(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # steps to print the linked list
    def printLL(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next

def reverseList(list):

  before = None
  current = list.head
  next = current.next

  # repeat this process till the final element of the list
  while current:
      current.next = before
      before = current
      current = next
      if next:
          next = next.next

  list.head = before



LL = LinkedList()
n=int(input("Enter the no.of element for linked list:"))
i=0
for i in range(n):
    a=int(input("Enter the element" ))
    LL.insert(a)
    i = 1 + 1

print("Linked List")
LL.printLL()
print("Reversed Linked List")
reverseList(LL)
LL.printLL()
