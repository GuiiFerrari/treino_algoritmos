from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: "ListNode") -> bool:
        if not other:
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        head_node = ListNode(val=None)
        current_node = head_node
        while head:
            seek_node = head
            is_unique = True
            while True:
                if not head.next:
                    break
                if seek_node.val != head.next.val:
                    break
                is_unique = False
                head = head.next
            if is_unique:
                current_node.next = seek_node
                current_node = current_node.next
            head = head.next
        if current_node:
            current_node.next = None
        return head_node.next
