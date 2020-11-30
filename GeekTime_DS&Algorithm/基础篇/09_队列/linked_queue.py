"""
    Queue based upon linked list
    链表实现队列

    date : 11-30-2020
"""


from typing import Optional

class LinkedNode:

    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class LinkedQueue:

    def __init__(self):
        self.head: Optional[LinkedNode] = None
        self.tail: Optional[LinkedNode] = None

    def enqueue(self, item):
        print("入队：", item)
        new_node = LinkedNode(item)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self) -> Optional[int]:
        print("出队")
        if self.head:
            val = self.head.val
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return val

    def __repr__(self):
        items = []
        cur = self.head     # 用一个指针指向队头结点，而不是直接移动队头结点
        while cur:
            items.append(str(cur.val))
            cur = cur.next
        return "->".join(item for item in items)


if __name__ == '__main__':
    linkQueue = LinkedQueue()
    linkQueue.enqueue(1)
    linkQueue.enqueue(2)
    linkQueue.enqueue(3)
    print(linkQueue)
    linkQueue.dequeue()
    linkQueue.dequeue()
    print(linkQueue)

