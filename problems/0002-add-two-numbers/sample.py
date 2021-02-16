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
        l = len(l1) - len(l2)

        if l > 0:
            arr = [0] * (l)
            l1.extend([0])
            l2.extend(arr)
        elif l < 0:
            arr = [0] * (-l)
            l2.extend([0])
            l1.extend(arr)
        else:
            l1.extend([0])
            l2.extend([0])

        length = int((len(l1) + len(l2))/2)

        for i in range(length):
            total = l1[i] + l2[i] + carry
            carry = int(total/10)
            current.next = ListNode(total%10)
            current = current.next

        if carry==1:
            current.next = ListNode(1)
            current = current.next

        return instance.next

# output = 708
#l1 = [2,4,3]
#l2 = [5,6,4]
# output = 0
#l1 = [0]
#l2 = [0]
# output = 89990001
l2 = [9,9,9,9,9,9,9]
l1 = [9,9,9,9]
instance = Solution()
obj = instance.addTwoNumbers(l1, l2)

while obj.next != None:
    print(obj.val, end='')
    obj = obj.next
print(obj.val, end='')

