class Node:
    def __init__(self, info, link = None):
        self.info = info
        self.link = link
class Stacks:
    def __init__(self):
        self.head = None
        self.top = self.head

    def Push(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
            self.top = self.head
        else:
            self.head.link = self.head
            self.head = newNode
            self.top = self.head
    
    def Pop(self):
        if self.head == None:
            return -1
        else:
            temp = self.top.next
            self.head = temp
            self.top = temp



#######
class Node:
    def __init__(self, info, link=None):
        self.info = info
        self.link = link

class Stack:
    def __init__(self):
        self.head = None  # Top of the stack

    def push(self, ele):
        new_node = Node(ele)
        new_node.link = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return -1
        popped_value = self.head.info
        self.head = self.head.link
        return popped_value

    def peek(self):
        if self.head is None:
            return -1
        return self.head.info

    def is_empty(self):
        return self.head is None

    def display(self):
        current = self.head
        if current is None:
            print("Stack is empty.")
        else:
            while current:
                print(current.info)
                current = current.link
