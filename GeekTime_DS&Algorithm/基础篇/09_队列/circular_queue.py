"""
    数组实现循环队列
    leetcode 622. 设计循环队列
    date : 11-30-2020
"""
from itertools import chain


class CircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k + 1
        self.items = [0 for _ in range(k + 1)]
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            print("enqueue:", value, "fail")
            return False
        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        print("enqueue:", value, "success")
        return True

    def deQueue(self):
        """
        Delete an element (head) from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            print("dequeue:", self.items[self.head])
            self.head = (self.head + 1) % self.capacity
            return True

    def Front(self):
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        print("Front item:", str(self.items[self.head]))

    def Rear(self):
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        print("Rear item:", self.items[self.tail - 1])

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == self.tail:
            print("Queue is empty!")
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.tail + 1) % self.capacity == self.head:
            print("Queue is full!")
            return True
        else:
            return False

    def __repr__(self) -> str:
        if self.tail >= self.head:
            return " -> ".join(str(item) for item in self.items[self.head: self.tail])
        else:
            return " -> ".join(str(item) for item in chain(self.items[self.head:], self.items[:self.tail]))


circularQueue = CircularQueue(3)  # 设置长度为
circularQueue.enQueue(1)
circularQueue.enQueue(2)
circularQueue.enQueue(3)
circularQueue.Front()
circularQueue.Rear()
print(circularQueue)
circularQueue.enQueue(4)  # 返回 false

circularQueue.isFull()  # 返回 true
circularQueue.deQueue()  # 返回 true
print(circularQueue)
circularQueue.enQueue(4)  # 返回true
print(circularQueue)
circularQueue.Rear()  # 返回4
circularQueue.Front()
