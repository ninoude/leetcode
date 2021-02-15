#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.
from IPython import embed

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        instance = ListNode()
        current = instance
        carry = 0
        length = 3

        for i in range(length):
            total = l1[i] + l2[i] + carry
            carry = int(total/10)
            current.next = ListNode(total%10)
            current = current.next
        return instance

l1 = [2,4,3]
l2 = [5,6,4]
instance = Solution()
obj = instance.addTwoNumbers(l1, l2)
