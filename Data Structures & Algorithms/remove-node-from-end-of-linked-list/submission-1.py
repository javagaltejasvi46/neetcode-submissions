# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return 
        l=head
        n=0
        while l:
            n+=1
            l=l.next
        if k == n:
            return head.next
        curr = head
        prev = head
        for _ in range(n-k):
            prev = curr
            curr = curr.next
        prev.next =curr.next
        curr.next = None
        return head


        
        