class ListNode:
    def __init__(self,val,nxt,prev):
        self.val=val
        self.nxt=nxt
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space=k
        self.lp=ListNode(0,None,None)
        self.rp=ListNode(0,None,self.lp)
        self.lp.nxt=self.rp

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        c=ListNode(value,self.rp,self.rp.prev)
        self.rp.prev.nxt=c
        self.rp.prev=c
        self.space-=1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.lp.nxt=self.lp.nxt.nxt
        self.lp.nxt.prev=self.lp
        self.space+=1
        return True

    def Front(self) -> int:
        if self.isEmpty():return -1
        return self.lp.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():return -1
        return self.rp.prev.val

    def isEmpty(self) -> bool:
        return self.lp.nxt==self.rp

    def isFull(self) -> bool:
        return self.space==0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()