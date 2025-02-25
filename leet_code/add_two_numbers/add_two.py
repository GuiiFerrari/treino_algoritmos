from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num = 0
        multiplier = 1
        ld1 = l1
        ld2 = l2
        while ld1 and ld2:
            num += (ld1.val + ld1.val) * multiplier
            multiplier = multiplier * 10
            ld1 = ld1.next
            ld2 = ld2.next
        curr_list = dummy_list = ListNode()
        for digit in str(num)[::-1]:
            curr_list.next = ListNode(val=int(digit))
            curr_list = curr_list.next
        return dummy_list.next
