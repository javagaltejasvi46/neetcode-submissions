# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l= list1
        r = list2
        result = ListNode()
        head = result
        while l and r:
            if l.val>r.val:
                result.next = r
                r=r.next
            else:
                result.next = l
                l=l.next
            result = result.next
        if l:
            while l:
                result.next = l
                l=l.next
                result=result.next
        elif r:
            while r:
                result.next = r
                r=r.next
                result=result.next
        return head.next
        