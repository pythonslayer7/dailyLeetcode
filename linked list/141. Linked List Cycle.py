from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # edge case where no head or head.next
        if not head or not head.next:
            return False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        # Time: O(N), N = num of nodes in the worst case
        # Space : O(1) because we only have fast, slow pointers
