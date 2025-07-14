from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prevNode, currNode, nexNode
        prevNode = None
        currNode = head

        while currNode:
            nexNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nexNode
        return prevNode
