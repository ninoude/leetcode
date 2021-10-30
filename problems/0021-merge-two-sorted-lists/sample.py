from typing import Optional

#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        answer_current = answer

        while l1 != None and l2 != None:
            if l2.val <= l1.val:
                answer_current.next = ListNode(l2.val)
                l2 = l2.next
            else:
                answer_current.next = ListNode(l1.val)
                l1 = l1.next
            answer_current = answer_current.next

        answer_current.next = l1 or l2

        return answer.next

