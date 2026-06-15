class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

  
        first = head
        second = prev

        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2