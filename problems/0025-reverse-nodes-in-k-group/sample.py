from typing import List
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        answer = point = ListNode(0)
        check = k % 2 #even or odd
        while head:
            arr.append(head.val)
            head = head.next
        for index,item in enumerate(arr):
            if (index+1) % k == 0:
                self.rearrangeArr(arr,index,k,check)

        for x in arr:
            point.next = ListNode(x)
            point = point.next
        return answer.next

    def rearrangeArr(self, arr, index, k, check):
        num = int(k/2)
        if check == 1:
            for i in range(num):
                tmp = arr[index-num-i-1]
                arr[index-num-i-1] = arr[index-num+i+1]
                arr[index-num+i+1] = tmp
        else:
            for i in range(num):
                tmp = arr[index-num-i]
                arr[index-num-i] = arr[index-num+1+i]
                arr[index-num+1+i] = tmp

