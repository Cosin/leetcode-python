# @File : 155-min-stack.py
# @Author : Shane Shek
# @Date : 2022-03-14 17:12:40
# @Desc : 最小栈

# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。 
# 
#  实现 MinStack 类: 
#
#  MinStack() 初始化堆栈对象。 
#  void push(int val) 将元素val推入堆栈。 
#  void pop() 删除堆栈顶部的元素。 
#  int top() 获取堆栈顶部的元素。 
#  int getMin() 获取堆栈中的最小元素。 
#
#  示例 1: 
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 输出：
# [null,null,null,null,-3,null,0,-2]
# 
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.

class MinStack:
    """
    需要辅助栈存最小值
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack.count != 0 and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        val = self.min_stack[-1]
        return val


class MinStack2:
    """
    无需辅助栈，把最小值和当前值作为数组存进栈
    """
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append([val, val if len(self.stack) == 0 or val <= self.stack[-1][1] else self.stack[-1][1]])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
