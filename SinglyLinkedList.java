// Class to create a new Node
class Node {
    int info;           // Stores the data
    Node link;          // Reference to the next node (like Python's "link")

    Node(int info) {
        this.info = info;
        this.link = null;
    }
}

// Class for the Linked List
class LinkedList {
    Node head;          // Points to the first node

    LinkedList() {
        this.head = null;
    }

    // Insert a node at the beginning
    void insertAtBeginning(int info) {
        Node newNode = new Node(info);  // Create new node

        if (head != null) {
            newNode.link = head;       // Point new node to old head
        }

        head = newNode;                // Make new node the head
    }

    // Optional: Print the list for verification
    void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.info + " -> ");
            temp = temp.link;
        }
        System.out.println("null");
    }
}
