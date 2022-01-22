from typing import List
from typing import Optional

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

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

