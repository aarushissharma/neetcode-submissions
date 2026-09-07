# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head 

        while curr: # continue until end of the list
            nxt = curr.next # temp var to store pointer

            curr.next = prev # reverse the pointer
            prev = curr
            curr = nxt

        return prev

        