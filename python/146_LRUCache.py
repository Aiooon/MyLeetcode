"""
146. LRU缓存机制
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；
        如果关键字不存在，则插入该组「关键字-值」。
        当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：
1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put

date : 11-11-2020
"""


# 定义双向链表
class DoubleLinkedListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


# 定义LRU缓存结构
class LRUCache:
    """
    思路：

    使用一个有序双向链表记录访问的结点，每个结点存储 key、value 两个信息及前驱、后继结点，越靠近链表尾部的结点表示越早访问。
    同时用一个 hash 表（字典）记录已在链表中的结点，存储结构为 {key: node}，即根据 key 值指向链表中对应的结点。
    这样就可以实现在 O(1) 的时间复杂度内查找。

    1. int get(int key):
    如果关键字 key 存在于 hash 表中，根据 {key: node} 找到链表中对应的结点，
    返回 node.value，并将该节点移动到链表表头。若不存在则返回-1.

    2. void put(int key, int value):
    如果关键字 key 存在于 hash 表中，根据 {key: node} 找到链表中对应的结点，更新其值为 value，并将其移动到链表表头。
    若 hash 表中不存在该 key， 则创建新的结点 node 存储 key-value，将 key-node 添加到 hash 表中，
    并将 node 添加到链表表头。若此时链表的长度超过了预先设定的最大缓存容量，则删除链表表尾结点。
    """

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    # 返回关键字的值
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        # print(node)
        return node.val

    # 插入新节点（若存在，更新值）
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DoubleLinkedListNode(key, value)
            self.cache[key] = node  # cache 中存的是节点
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                rem = self.removeTail()
                self.size -= 1
                self.cache.pop(rem.key)
        else:
            node = self.cache[key]
            self.moveToHead(node)
            node.val = value

    # 将结点添加到链表表头
    def addToHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # 删除结点
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    # 移到表头由两步完成：删除该节点、将该结点添加到表头
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    # 删除表尾结点
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    LRUcache = LRUCache(2)
    LRUcache.put(1, 1)
    LRUcache.put(2, 2)
    # print(LRUcache.cache)
    print(LRUcache.get(1))  # 返回  1
    LRUcache.put(3, 3)  # 该操作会使得密钥 2 作废
    # print(LRUcache.cache)
    print(LRUcache.get(2))  # 返回 -1 (未找到)
    LRUcache.put(4, 4)  # 该操作会使得密钥 1 作废
    # print(LRUcache.cache)
    print(LRUcache.get(1))  # 返回 -1 (未找到)
    print(LRUcache.get(3))  # 返回  3
    # print(LRUcache.cache)
    print(LRUcache.get(4))  # 返回  4
    # print(LRUcache.cache)
