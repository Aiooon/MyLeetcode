"""
155. 最小栈
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop() —— 删除栈顶的元素。
top() —— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。

示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

提示：pop、top 和 getMin 操作总是在 非空栈 上调用。

date: 1-14-2020
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
