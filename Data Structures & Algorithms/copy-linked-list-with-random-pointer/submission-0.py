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
        oltTocopy={None:None}
        cur=head

        while cur:
            copy=Node(cur.val)
            oltTocopy[cur]=copy
            cur=cur.next
        
        cur=head
        while cur:
            copy=oltTocopy[cur]
            copy.next=oltTocopy[cur.next]
            copy.random=oltTocopy[cur.random]
            cur=cur.next
        return oltTocopy[head]

        