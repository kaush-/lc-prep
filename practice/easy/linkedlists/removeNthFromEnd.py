from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        if head.next is None:
            return None

        first = head
        second = head
        pre = head

        for _ in range(n-1):
            first = first.next

        while first.next is not None:
            pre = second
            second = second.next
            first = first.next

        if pre == second:
            head = second.next
        else:
            pre.next = second.next

        return head