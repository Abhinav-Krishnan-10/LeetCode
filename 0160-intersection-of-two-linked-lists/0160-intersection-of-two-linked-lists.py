# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1 = headA
        ptr2 = headB
        cnt = 0
    
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
            if ptr1 == None:
                ptr1 = headB
                cnt += 1
            
            if ptr2 == None:
                ptr2 = headA
                cnt += 1
                
            if cnt > 2:
                return None
        
        return ptr1
        