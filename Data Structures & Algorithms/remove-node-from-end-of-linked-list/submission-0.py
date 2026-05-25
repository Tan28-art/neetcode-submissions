# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse linked list first
        first = head
        prev = None

        while first:
            tmp1 = first.next
            first.next = prev
            prev = first
            first = tmp1

        # prev is the head of the new reversed linked list
        head2 = prev

        # now we deleted the nth node from the head2

        if n == 1:
            # deleting the head
            if head2.next is None:
                return None
            else:
                newHead = head2.next
                head2.next = None
                head2 = newHead

        else:
            curr = head2
            prev2 = None
            
            for i in range(n-1):    
                prev2 = curr
                curr = curr.next
            
            tmp = curr.next
            prev2.next = tmp

            iterator = head2
         
        # now we must reverse the linked list back
        # head2 is our current head

        first = head2
        prev = None

        while first:
            tmp1 = first.next
            first.next = prev
            prev = first
            first = tmp1
    
        return prev



