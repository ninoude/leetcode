from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        head_len = 0

        while current.next != None:
            current = current.next
            head_len += 1

        pop_index = head_len + 1 - n

        current = head
        ln_len = 0

        answer = ListNode()
        answer_current = answer

        while current.next != None:
            if ln_len == pop_index:
                current = current.next
                ln_len += 1
                continue
            answer_current.next = ListNode(current.val)
            answer_current = answer_current.next
            current = current.next
            ln_len += 1

        if ln_len == pop_index:
            return answer.next
        else:
            answer_current.next = ListNode(current.val)
            return answer.next

l1_list = [1,2,3,4,5]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

test = Solution()
answer = test.removeNthFromEnd(l1.next, 2)

for i in range (len(l1_list)-1):
    print(answer.val)
    answer = answer.next

l1_list = [1]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

test = Solution()
answer = test.removeNthFromEnd(l1.next, 1)

for i in range (len(l1_list)-1):
    print(answer.val)
    answer = answer.next

l1_list = [1,2]
l1 = ListNode()
l1_current = l1

for i in range(len(l1_list)):
    l1_current.next = ListNode(l1_list[i])
    l1_current = l1_current.next

test = Solution()
answer = test.removeNthFromEnd(l1.next, 1)

for i in range (len(l1_list)-1):
    print(answer.val)
    answer = answer.next
