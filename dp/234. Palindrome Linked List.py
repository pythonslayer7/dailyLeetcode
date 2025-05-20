
from typing import Optional 
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next # slow gives the middle node
            fast = fast.next.next
        reversedNode = self.reverseNodes(slow)

        # compare the reversedNode to head to check for palindrome
        while reversedNode:
            if head.val != reversedNode.val:
                return False
            head = head.next
            reversedNode = reversedNode.next
        return True

    def reverseNodes(self, head):
        prevNode = None
        currNode = head
        while currNode:
            #save next node
            nextNode = currNode.next
            #reverse pointer to prevNode
            currNode.next = prevNode
            #reassign prevNode to currNode
            prevNode = currNode
            #reassign currNode to nextNode
            currNode = nextNode
        return prevNode
