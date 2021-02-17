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

        while l1.next != None and l2.next != None:
            if l1.next != None:
                l1_v = l1.val
                l1 = l1.next
            else:
                l1_v=0

            if l2.next != None:
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

# output = 708
#l1_list = [2,4,3]
#l2_list = [5,6,4]
# output = 0
l1_list = [0]
l2_list = [0]
# output = 89990001
#l2 = [9,9,9,9,9,9,9]
#l1 = [9,9,9,9]

l1 = ListNode()
l1_current = l1
l2 = ListNode()
l2_current = l2

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

for i in range(len(l2_list)):
    l2_current.next = ListNode(l2_list[i])
    l2_current = l2_current.next

instance = Solution()
obj = instance.addTwoNumbers(l1.next, l2.next)

while obj.next != None:
    print(obj.val, end='')
    obj = obj.next
print(obj.val, end='')

