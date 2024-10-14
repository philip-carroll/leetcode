# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head is not None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev


if __name__ == '__main__':
    sol = Solution()

    rev = sol.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))

    while rev:
        print(rev.val)
        rev = rev.next
