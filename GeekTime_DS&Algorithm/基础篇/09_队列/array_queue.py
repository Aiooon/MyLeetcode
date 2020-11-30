"""
    Queue based upon array
    用数组实现的队列

    date : 11-24-2020
"""

from typing import Optional


class ArrayQueue:

    def __init__(self, capacity: int):
        self.items = []     # 队列元素
        self.capacity = capacity    # 最大存储空间
        self.head = 0       # 队头指针
        self.tail = 0       # 队尾指针

    def enqueue(self, item: str) -> bool:
        print("入队：", item)
        if self.tail == self.capacity:   # 队满
            if self.head == 0:
                print("队满!")
                return False
            else:   # 队头前有空余，数据搬移
                for i in range(0, self.tail - self.head):
                    self.items[i] = self.items[i + self.head]
                self.tail = self.tail - self.head
                self.head = 0

        self.items.insert(self.tail, item)
        self.tail += 1
        print("入队成功")
        return True

    def dequeue(self) -> Optional[str]:
        """
        关于 Optional 的使用：
        每当你有一个默认值 None 的关键字参数时，你应该使用 Optional。
        Optional[Union[str, int]] 和 Union[str, int, None] 完全相同。

        """
        if self.head != self.tail:
            item = self.items[self.head]
            self.head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        return "->".join(item for item in self.items[self.head: self.tail])


arrQue = ArrayQueue(3)
arrQue.enqueue("1")
arrQue.enqueue("2")
arrQue.enqueue("3")
print(arrQue)
arrQue.dequeue()
arrQue.dequeue()
print(arrQue)
