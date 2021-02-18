#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        instance = ListNode()
        current = instance
        carry = 0

        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_v = l1.val
                l1 = l1.next
            else:
                l1_v=0

            if l2 is not None:
                l2_v = l2.val
                l2 = l2.next
            else:
                l2_v=0

            total = l1_v + l2_v + carry
            carry = int(total/10)
            current.next = ListNode(total%10)
            current = current.next

        if carry==1:
            current.next = ListNode(1)
            current = current.next

        return instance.next
