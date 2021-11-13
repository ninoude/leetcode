from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

l1_list = [1,4,5]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

l2_list = [1,3,4]
l2 = ListNode()
l2_current = l2

for i in range(len(l2_list)):
    l2_current.next = ListNode(l2_list[i])
    l2_current = l2_current.next

l3_list = [2,6]
l3 = ListNode()
l3_current = l3

for i in range(len(l3_list)):
    l3_current.next = ListNode(l3_list[i])
    l3_current = l3_current.next

test = Solution()
answer = test.mergeKLists([l1.next, l2.next, l3.next])

print("1->1->2->3->4->4->5->6")
while answer != None:
    print(answer.val)
    answer = answer.next

