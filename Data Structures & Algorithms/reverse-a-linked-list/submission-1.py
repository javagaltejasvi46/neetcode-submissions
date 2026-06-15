# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None 
        if head.next == None:
            return head
        after = head
        temp = head
        before = None
        while after.next :
            head = head.next
            after = temp.next
            temp.next = before 
            before = temp
            temp = after
        temp.next = before
        return temp

        

        