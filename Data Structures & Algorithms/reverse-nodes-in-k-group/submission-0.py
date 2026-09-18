# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        gp=dummy

        while True:
            kth=self.getK(gp,k)
            if not kth:
                break
            gpn=kth.next

            prev,cur=kth.next,gp.next
            while cur!=gpn:
                tmp=cur.next
                cur.next=prev
                prev=cur
                cur=tmp
            
            tmp=gp.next
            gp.next=kth
            gp=tmp
        return dummy.next

    def getK(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur