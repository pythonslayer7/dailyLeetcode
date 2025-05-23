from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow is the middle node
        # we reverse from the tail until the middle node
        secondList = self.reverse(slow.next)
        slow.next = None
        # merge the 2 lists
        firstList = head
        while secondList:
            temp1 = firstList.next
            temp2 = secondList.next

            firstList.next = secondList
            secondList.next = temp1

            firstList = temp1
            secondList = temp2

    def reverse(self, head):
        prevNode = None
        currNode = head
        while currNode:
            # save the next node
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return prevNode # this is the tail

