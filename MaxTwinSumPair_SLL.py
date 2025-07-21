class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head) -> int:
        # Define a function to reverse a linked list
        def reverse_list(node):
            prev = None
            current_node = node
            # Iterate through the list and reverse the links
            while current_node:
                next_node = current_node.next
                current_node.next = prev
                prev = current_node
                current_node = next_node
            return prev

        # Initialize slow and fast pointers to find the middle of the linked list
        slow_pointer, fast_pointer = head, head.next
        while fast_pointer and fast_pointer.next:
            slow_pointer, fast_pointer = slow_pointer.next, fast_pointer.next.next
      
        # Split the list into two halves
        first_half_head = head
        second_half_start = slow_pointer.next
        slow_pointer.next = None  # Break the list to create two separate lists
      
        # Reverse the second half of the list
        second_half_head = reverse_list(second_half_start)
      
        # Initialize the answer to zero
        max_pair_sum = 0
      
        # Traverse both halves simultaneously and find the max pair sum
        while first_half_head and second_half_head:
            current_pair_sum = first_half_head.val + second_half_head.val
            max_pair_sum = max(max_pair_sum, current_pair_sum)
            first_half_head = first_half_head.next
            second_half_head = second_half_head.next
      
        # Return the maximum pair sum found
        return max_pair_sum
