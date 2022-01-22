from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        answer = point = ListNode(0)
        while head:
            arr.append(head.val)
            head = head.next
        for index,item in enumerate(arr):
            if (index+1) % 2 == 0:
                tmp = arr[index-1]
                arr[index-1] = item
                arr[index] = tmp
        for x in arr:
            point.next = ListNode(x)
            point = point.next
        return answer.next

l1_list = [1,2,3,4]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

test = Solution()
answer = test.swapPairs(l1.next)

print('[2,1,4,3]')
while answer:
    print(answer.val)
    answer = answer.next

l1_list = [1]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

test = Solution()
answer = test.swapPairs(l1.next)

print('[1]')
while answer:
    print(answer.val)
    answer = answer.next
