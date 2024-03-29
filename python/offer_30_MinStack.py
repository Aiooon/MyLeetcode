"""
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.

提示：各函数的调用总次数不超过 20000 次
注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

date : 1-14-2020
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)
        if not self.stackB or x <= self.stackB[-1]:
            self.stackB.append(x)

    def pop(self) -> None:
        if self.stackA.pop() == self.stackB[-1]:
            self.stackB.pop()

    def top(self) -> int:
        return self.stackA[-1]

    def min(self) -> int:
        return self.stackB[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.min())
    minStack.pop()
    minStack.top()
    print(minStack.min())
