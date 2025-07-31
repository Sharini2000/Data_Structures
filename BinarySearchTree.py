## Iterative Method --->
class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None

class BinarySearchTree:  
    def __init__(self):
        self.root = None

    def insertBST(self,key):
        temp = Node(key)

        if self.root is None:
            self.root = temp
        else:
            curr = self.root
            parent = None

            while curr is not None:
                parent = curr
                if curr.key > key:
                    curr = curr.left
                elif curr.key < key:
                    curr = curr.right
                else:
                    curr = None  
                    """ If key already exists we don't have to add 
            it in BST, so I have to stop the while loop by giving 
            curr value to be None"""
            
            if parent.key > key:
                parent.left = temp
            else:
                parent.right = temp
    
    def inorderTraversal(self,root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key, end=" ")
            self.inorderTraversal(root.right)

BST = BinarySearchTree()
BST.insertBST(50)
BST.insertBST(30)
BST.insertBST(20)
BST.insertBST(40)
BST.insertBST(60)
BST.insertBST(70)
BST.inorderTraversal(BST.root)


# Recursive method

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.binaryTree(nums, 0, len(nums) -1)
        
    def binaryTree(self, nums: List[int], i:int, j:int) -> Optional[TreeNode]:
        if i>j:
            return None
        mid = (i+j)//2
        node = TreeNode(nums[mid])
        node.left = self.binaryTree(nums, i, mid-1)
        node.right = self.binaryTree(nums, mid+1, j)
        return node