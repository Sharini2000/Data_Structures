# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Why head.next too? ->  Bcoz if there is only one ele, it has to be deleted.
        if not head or not head.next:
            return None

        current = head
        size = 0
        while current:
            size += 1
            current = current.next
        
        middle_index = int(size / 2)
        current = head
        for i in range(middle_index-1):
            current = current.next

        current.next = current.next.next

        return head
    


# Alternate method using slow/fast pointers

        """ In this algorithm, we get three usable output details as a result.
        1. The slow pointer will hold the middle elements' value at the final loop.
        2. The prev will have the value of middle's previous element.
        3. The fast pointer will have the value of last ele in SLL.

        Slow pointer increments by 1 and fast pointer increments by 2. This way the LL can be traversed       faster.
        """
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: only one node
        if not head or not head.next:
            return None

        prev = None
        slow = head
        fast = head

        # Move slow by 1 and fast by 2
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev.next = slow.next

        return head



"""
Question :
2095. Delete the Middle Node of a Linked List
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
 

"""