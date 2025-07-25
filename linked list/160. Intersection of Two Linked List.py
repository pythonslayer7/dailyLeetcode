from typing import Optional 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        newA, newB = headA, headB
        if not headA or not headB:
            return None
        # comparing their reference address, not actual node val    
        while newA != newB:
            newA = newA.next if newA else headB
            newB = newB.next if newB else headA
        return newA