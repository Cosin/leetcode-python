# @File : 20-valid-parentheses.py
# @Author : Shane Shek
# @Date : 2021-01-21 23:04:58
# @Desc : 有效的括号

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true


class StackNode:
    def __init__(self, value, top):
        self.value = value
        self.next = top


class Stack:
    def __init__(self):
        self.count = 0
        self.top: StackNode = None

    def push(self, node: StackNode):
        node.next = self.top
        self.count = self.count + 1
        self.top = node

    def pop(self):
        tmp: StackNode = self.top
        self.top = tmp.next
        self.count = self.count - 1
        del tmp


class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        stack = Stack()
        m = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        for c in s:
            if c == " ":
                continue
            elif stack.top is None or c in "({[":
                node = StackNode(c, stack.top)
                stack.push(node)
            else:
                if m[c] == stack.top.value:
                    stack.pop()
                else:
                    return False
        if stack.count is 0:
            return True
        else:
            return False
