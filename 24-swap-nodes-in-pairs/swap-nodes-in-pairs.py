# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Swapping
            first.next = second.next
            second.next = first
            current.next = second
            
            # Move pointer forward for the next pair
            current = first
            
        return dummy.next