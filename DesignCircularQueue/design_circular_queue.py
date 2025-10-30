"""
Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.
"""

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxLen = k
        self.front = 0
        self.rear = 0
    
    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxLen
            return True
        else:
            return False
    
    def deQueue(self) -> bool:
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxLen
            return True
  
    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]
  
    def Rear(self) -> int:
        return -1 if self.q[self.rear] is None else self.q[self.rear]
  
    def isEmpty(self) -> bool:
        return self.front == self.rear and self.q[self.front] is None
  
    def isFull(self) -> bool:
        return self.front == self.rear and self.q[self.front] is not None


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(2)
param_1 = obj.enQueue(1)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()