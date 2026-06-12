# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr is not None:
            # find curr.next
            temp = curr.next
            # we want to make curr.next be linked to prev
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev