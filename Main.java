public class Main {
    public static void main(String[] args) {
        LinkedList LL = new LinkedList();
        LL.insertAtBeginning(10);
        LL.insertAtBeginning(20);
        LL.insertAtBeginning(30);

        LL.printList(); // Optional: Output will be 30 -> 20 -> 10 -> null
    }
}
