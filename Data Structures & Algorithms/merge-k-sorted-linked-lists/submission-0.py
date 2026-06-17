class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        result = None

        for lst in lists:
            result = self.merge(result, lst)

        return result

    def merge(self, a, b):
        dummy = ListNode()
        tail = dummy

        while a and b:
            if a.val <= b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next

            tail = tail.next

        if a:
            tail.next = a
        else:
            tail.next = b

        return dummy.next