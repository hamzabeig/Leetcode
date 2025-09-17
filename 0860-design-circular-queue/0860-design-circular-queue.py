class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.space = k
        self.front = 0
        self.rear = -1
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear +1) % self.size
        self.q[self.rear] = value
        self.space -= 1
        return True
         

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front +1) % self.size
        # self.q[self.front]= None
        self.space+=1
        return True        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]
        

    def isEmpty(self) -> bool:
        return self.space == self.size
        

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