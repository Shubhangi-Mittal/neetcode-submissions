# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        lp,c=dummy,head

        for i in range(left-1):
            lp,c=c,c.next  #reaching l to start reversing

        p=None
        for i in range(right-left+1): #reversing links in range l to r
            t=c.next
            c.next=p
            p,c=c,t 

        lp.next.next=c #updating pointers for lth and rth elements
        lp.next=p
        return dummy.next
