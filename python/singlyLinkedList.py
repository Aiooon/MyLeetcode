# Definition for singly-linked list.
"""
需要修改：
新建 SinglyLinkedList 类与结点区分开，并实现内部方法

"""

from typing import List, Optional


class Node:
    """单链表结构的 Node节点"""

    def __init__(self, data: int, next_node=None):
        """
        Node节点的初始化方法
        :param data: 存储的数据
        :param next_node: 下一个 Node节点的引用地址
        """
        self.data = data
        self.next = next_node

    # @property
    # def data(self):
    #     return self.data
    #
    # @data.setter
    # def data(self, data):
    #     self.data = data
    #
    # @property
    # def next_node(self):
    #     return self.next
    #
    # @next_node.setter
    # def next_node(self, next_node):
    #     self.next = next_node


class SinglyLinkedList:
    """单向链表"""

    def __init__(self):
        """
        单链表的初始化
        """
        self.head = None

    def insert_to_head(self, value: int):
        """
        在链表的头部插入一个存储 value数值的 Node节点.
        参数:
            value:将要存储的数据
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_to_tail(self, value: int):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert_after(self, node: Node, value: int):
        """
        在链表的某个指定 Node节点之后插入一个存储 value数据的 Node节点.
        参数:
            node:指定的一个 Node节点
            value:将要存储在新 Node节点中的数据
        """
        if node is None:  # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def insert_before(self, node: Node, value: int):
        """
        在链表的某个指定 Node节点之前插入一个存储 value数据的 Node节点.
        参数:
            node:指定的一个Node节点
            value:将要存储在新的Node节点中的数据
        """
        if (node is None) or (self.head is None):  # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
            return

        if node == self.head:  # 如果是在链表头之前插入数据节点，则直接插入
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.head
        not_found = False  # 如果在整个链表中都没有找到指定插入的Node节点，则该标记量设置为True
        while pro.next != node:  # 寻找指定Node之前的一个Node
            if pro.next is None:  # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pro = pro.next
        if not not_found:
            pro.next = new_node
            new_node.next = node

    def delete_by_node(self, node: Node):
        """
        在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
        if not self.head or not node:
            return

        if node == self.head:  # 如果指定删除的Node节点是链表的头节点
            self.head = node.next
            return

        pro = self.head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next != node:
            if pro.next is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next
        if not not_found:
            pro.next = node.next

    def delete_by_value(self, value: int):
        """
        在链表中删除指定存储数据的Node节点.
        参数:
            value:指定的存储数据
        """
        if self.head is None:  # 如果链表是空的，则什么都不做
            return

        if self.head.data == value:  # 如果链表的头Node节点就是指定删除的Node节点
            self.head = self.head.next

        pro = self.head
        node = self.head.next
        not_found = False
        while node.data != value:
            if node.next is None:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到执行Value值的Node节点
                not_found = True
                break
            else:
                pro = node
                node = node.next
        if not_found is False:
            pro.next = node.next

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        fast = self.head
        slow = self.head
        step = 0

        while step <= n:
            fast = fast.next
            step += 1
        tmp = None
        while fast.next is not None:
            tmp = slow
            fast = fast.next
            slow = slow.next

        tmp.next_node = slow.next

    def find_by_value(self, value: int) -> Optional[Node]:
        """
        按照数据值在单向列表中查找.
        参数:
            value:查找的数据
        返回:
            Node
        """
        node = self.head
        while node and node.data != value:
            node = node.next
        return node

    def find_by_index(self, index: int) -> Optional[Node]:
        """
        按照索引值在列表中查找.
        参数:
            index:索引值
        返回:
            Node
        """
        node = self.head
        pos = 0
        while node and pos != index:
            node = node.next
            pos += 1
        return node

    def find_mid_node(self):
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """
        fast = self.head
        slow = self.head

        while fast.next_node is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def create_node(self, value):
        """创建一个存储value值的Node节点.
        参数:
            value:将要存储在Node节点中的数据
        返回:
            一个新的Node节点
        """
        return Node(value)

    def reversed_self(self):
        """翻转链表自身."""
        if self.head is None or self.head.next is None:  # 如果链表为空，或者链表只有一个节点
            return

        pre = self.head
        node = self.head.next
        while node is not None:
            pre, node = self._reversed_with_two_node(pre, node)

        self.head.next = None
        self.head = pre

    def _reversed_with_two_node(self, pre, node):
        """翻转相邻两个节点.
        参数:
            pre:前一个节点
            node:当前节点
        返回:
            (pre,node):下一个相邻节点的元组
        """
        tmp = node.next
        node.next = pre
        pre = node  # 这样写有点啰嗦，但是能让人更能看明白
        node = tmp
        return pre, node

    def has_ring(self):
        """检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环
        """
        fast = self.head
        slow = self.head

        while (fast.next is not None) and (fast is not None):
            fast = fast.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    def buildList(self, nums: List):
        """
        根据列表创建链表
        :param nums: input int list to build Singly Linked List
        :return: head of the built Singly Linked List
        """
        for num in nums:
            self.insert_to_tail(num)

    # 打印链表
    def __repr__(self) -> str:
        nums = []
        cur = self.head
        while cur:
            nums.append(cur.data)
            cur = cur.next
        return " -> ".join(str(num) for num in nums)

    # 重写__iter__方法，方便for关键字调用打印值
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def print_all(self):
        """打印当前链表所有节点数据."""
        cur = self.head
        """
        print字符串前面加f表示格式化字符串，
        加f后可以在字符串里面使用用花括号括起来的变量和表达式，
        如果字符串里面没有表达式，那么前面加不加f输出应该都一样.
        """
        if cur:
            print(f"{cur.data}", end="")
            cur = cur.next
        while cur:
            print(f" -> {cur.data}", end="")
            cur = cur.next
        print("\n", flush=True)

    # Reverse Linked List
    def reverseList(self):
        """

        :param head: head node of the Linked List
        :return: new head
        """
        cur = self.head
        reverse_head = None
        while cur:
            next = cur.next
            cur.next = reverse_head
            reverse_head = cur
            cur = next
        self.head = reverse_head

    # Length of Linked List
    def length(self) -> int:
        if not self.head:
            return 0
        l = 0
        cur = self.head
        while cur:
            l += 1
            cur = cur.next
        return l


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    linkedList = SinglyLinkedList()
    linkedList.buildList(nums)
    print(linkedList)
    linkedList.reverseList()
    print(linkedList)
    print("---------------------------")
    linkedList.insert_to_head(0)
    linkedList.insert_to_tail(6)
    node3 = linkedList.find_by_value(3)
    linkedList.insert_after(node3, 4)
    linkedList.insert_before(node3, 2)
    linkedList.print_all()
    print(linkedList.find_by_index(6).data)
    print("length:", linkedList.length())
    print(linkedList)
