class Node:
    def __init__(self,info,prev=None,next=None):
        self.info = info
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,info):
        newNode = Node(info)   

        if self.head != None:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

        else:
            self.head = newNode

            
    def insert_at_end(self,info):

        newNode = Node(info)
        
        if self.head != None:
            current = self.head
            while current.next != None:
                current = current.next
            newNode.prev = current
            current.next = newNode
        
        else:
            self.head = newNode

    def delete_node(self, ele):
        if self.head == None:
            print("List empty")
            return
        # If only one element is present
        if self.head.next == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp = None
                return
            else:
                print("Element not found in the list")

        #Delete node in between
        temp = self.head.next
        while temp.next != None:
            if temp.info == ele:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp = None
                return 
            temp = temp.next

        #Delete last node
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        print("element not found")

        
    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.next


DL = DoublyLinkedList()
DL.insert_at_beginning(10)
DL.display()
print("###")
DL.insert_at_end(5)
DL.display()
print("###")
DL.insert_at_end(15)
DL.insert_at_end(20)
DL.display()
print("###")
DL.delete_node(15)
DL.display()