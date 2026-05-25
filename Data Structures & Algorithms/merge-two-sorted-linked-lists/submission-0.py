# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        sortedLinkedList = head

        while list1 and list2:
            if list1.val < list2.val:
                sortedLinkedList.next = list1
                list1 = list1.next

            else:
                sortedLinkedList.next = list2
                list2 = list2.next

            sortedLinkedList = sortedLinkedList.next

        # case where one of the linked list still has nodes remaining
        if list1:
            sortedLinkedList.next = list1
        elif list2:
            sortedLinkedList.next = list2

        return head.next
