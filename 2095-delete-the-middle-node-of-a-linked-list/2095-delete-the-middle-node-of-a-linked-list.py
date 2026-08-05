# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if head is None or head.next is None:
                return None

        n = 0
        ptr = head
        while ptr != None:
            n += 1
            ptr = ptr.next

        mid = n // 2

        ptr = head
        for i in range(mid - 1):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head