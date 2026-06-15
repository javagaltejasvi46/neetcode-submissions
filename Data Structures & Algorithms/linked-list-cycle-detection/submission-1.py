# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = []
        i=head
        while i:
            if i in temp:
                return True 
            temp.append(i)
            i=i.next
        return False

        