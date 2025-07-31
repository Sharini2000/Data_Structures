class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKGroup(head, k):
    if head is None:
        return head

    curr = head
    newHead = None
    tail = None

    while curr is not None:
        groupHead = curr
        prev = None
        nextNode = None
        count = 0

        while curr is not None and count < k:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            count += 1

        if newHead is None:
            newHead = prev

        if tail is not None:
            tail.next = prev

        tail = groupHead

    return newHead

def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Creating a sample singly linked list:
    # 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    head = reverseKGroup(head, 3)
    printList(head)