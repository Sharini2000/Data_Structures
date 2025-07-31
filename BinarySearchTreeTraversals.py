class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class buildBST:
    def __init__(self):
        self.root = None
    
    def buildingBST(self,val):
        temp = Node(val)
        if self.root is None:
            self.root = temp
        
        curr = self.root
        parent = None

        while curr:
            parent = curr
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                curr = None
        
        if parent.val < val:
            parent.right = temp
        elif parent.val > val:
            parent.left = temp

        return self.root
    
    def inorder_iterative(self,root):
        #Append the elements in the order you want to pop to print.
        # Step 1 : Append the root in stack
        # Step 2: Append all the left nodes in stack until it's None
        # Step 3: Pop the last left element and print
        # Step 4: Assign the curr value to refernce to last left element's right
        # Repeat Step 1 to 4
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.val)
                current = current.right
            else:
                break

    def inorder_recursive(self,root):
        if root:
            self.inorder_recursive(root.left)
            print(root.val)
            self.inorder_recursive(root.right)

    def preorder_iterative(self,root):
        """ Algorithm:-
        Initialize an empty stack.
        If the root is None, return immediately (nothing to traverse).
        Push the root node onto the stack.
        While the stack is not empty, repeat steps 5–7:
        Pop a node from the stack. Let's call it current.
        Process current (print its value).
        If current has a right child, push it onto the stack.
        If current has a left child, push it onto the stack."""
            
        if root is None:
            return
        stack = []
        current = root
        stack.append(root)
        while stack:
            
            current = stack.pop()
            print(current.val)
                
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

    def preorder_recursive(self,root):
        if root:
            print(root.val)
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)   

    def postorder_recursive(self,root):
        if root:
            self.preorder_recursive(root.left)
            self.preorder_recursive(root.right)  
            print(root.val)   

    def postorder_iterative(self,root):
        
        if root is None:
            return
        stack = []
        current = root
    
        while True:     
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
            else:
                stack.append(current)
                current = stack.pop()
                print(current.val)
                current = current.left
            

        


BST = buildBST()
BST.buildingBST(50)
BST.buildingBST(40)
BST.buildingBST(60)
BST.buildingBST(30)
BST.buildingBST(70)
BST.buildingBST(45)
BST.buildingBST(55)
print("Indorder traversal - Iterative method")
BST.inorder_iterative(BST.root)
print("Indorder traversal - Recursive method")
BST.inorder_recursive(BST.root)
print("Preorder traversal - Iterative method")
BST.preorder_iterative(BST.root)
print("Preorder traversal - Recursive method")
BST.preorder_recursive(BST.root)
print("Postorder traversal - Recursive method")
BST.postorder_recursive(BST.root)

