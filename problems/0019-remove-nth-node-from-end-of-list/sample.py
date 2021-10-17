from typing import Optional

#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        tmp = head
        size = 0

        # find the size of the linked list
        while tmp:
            size += 1
            tmp = tmp.next
        tmp = head

        #if we have to remove the first node:
        if n == size:
            return head.next

        for i in range(size-n-1):
            tmp = tmp.next
        tmp.next = tmp.next.next
        return head

