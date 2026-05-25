# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding mid point of linked list first

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow.next is the head of the second half of the list
        head2 = slow.next
        slow.next = None
        prev = None
        # now we  must reverse this second list

        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            head2 = nxt

        # now the head of the reversed list is prev
        headReversed = prev
        head1 = head

        # Now we merge the two lists together
        while headReversed:
            head1Nxt = head1.next
            headReversedNxt = headReversed.next

            head1.next = headReversed
            headReversed.next = head1Nxt

            head1 = head1Nxt
            headReversed = headReversedNxt


        
            





