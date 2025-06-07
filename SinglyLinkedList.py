# Class to create a new node. In C, we use struct instead. But in c++/Java or Python, we use a class to create a node.
class Node:
    def __init__(self, info, link=None):
        self.info = info # Data type - int
        self.link = link # It stores the entire data of next node. It's a reference variable unlike normal variable. Data type : Node

class LinkedList:
    def __init__(self):
        self.head = None # Same as link. But it stores the entire first node. Data type - node

    def insert_at_beginning(self,info):

        newNode = Node(info)
        if self.head != None:
            newNode.link = self.head
            self.head = newNode

        else:
            self.head = newNode

    def insert_at_end(self,info):

        newNode = Node(info)

        if self.head != None:
            current_node = self.head
            while current_node.link != None:
                current_node = current_node.link

            current_node.link = newNode

        else:
            self.head = newNode

    # def insert_at_position(self,info):
    #     count = 0
    #     newNode = Node(info)

    #     if self.head != None:
    #         current_node = self.head

    #         while count < 2:
    #             current_node = current_node.link
    #             count += 1

    #         current_node.link = newNode

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link


LL = LinkedList()
LL.insert_at_beginning(10)
LL.insert_at_beginning(5)
LL.display()
LL.insert_at_end(15)
LL.insert_at_end(20)
LL.display()

    

    