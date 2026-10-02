# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes remaining
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
            
            group_next = kth.next

            # Reverse the k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Update connections for the reversed group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next

    def getKthNode(self, curr: ListNode | None, k: int) -> ListNode | None:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr