class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next = next

class CircularSinglyLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,info):

        newNode = Node(info)

        if self.head is None:
            newNode.next = newNode
            #This is the property of Circular LL. If the list is empty, the head should point to itself.
            self.head = newNode

        else:
            # Let's first traverse to find the last element in the list
            current = self.head
            while current.next != self.head:
                current = current.next

            # Now let's insert the ele at first and point the head to next and point the last ele's next to head.
            newNode.next = self.head
            self.head = newNode
            current.next = self.head

    def display(self):
        if self.head is None:
            print("List empty")
            return
        else:
            current = self.head
            while True:
                print(current.info)
                current = current.next
                if current == self.head:
                    break
            return

CSLL = CircularSinglyLinkedList()
CSLL.insert_at_beginning(10)
CSLL.insert_at_beginning(5)
print("####")
CSLL.display()
