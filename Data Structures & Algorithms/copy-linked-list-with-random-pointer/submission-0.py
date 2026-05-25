"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        hashMap = {None: None}
        cur = head

        # responsible for copying the nodes
        while cur:
            copy = Node(cur.val) # no linking done only makes copies with the values
            hashMap[cur] = copy # maps the original node to the copy
            cur = cur.next

        # responsible for the linking of the nodes in the deep copy
        cur = head
        while cur:
            copy = hashMap[cur]
            copy.next = hashMap[cur.next]
            copy.random = hashMap[cur.random]
            cur = cur.next

        return hashMap[head]
        