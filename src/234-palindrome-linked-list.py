# @File : 234-palindrome-linked-list.py
# @Author : Shane Shek
# @Date : 2021-11-30 13:17:50
# @Desc : 回文链表

# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
#
#  示例 1： 
#
# 输入：head = [1,2,2,1]
# 输出：true
#
#  示例 2： 
#
# 输入：head = [1,2]
# 输出：false
#
#  提示： 
# 
#  链表中节点数目在范围[1, 10⁵] 内
#  0 <= Node.val <= 9 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


tmp: ListNode

class Solution:

    # Recursion
    def isPalindrome(self, head: ListNode) -> bool:
        global tmp
        tmp = head
        return self.check(head)

    def check(self, head: ListNode) -> bool:
        global tmp
        if head is None:
            return True
        res = self.check(head.next) and (head.val == tmp.val)
        tmp = tmp.next
        return res

    # array
    def isPalindrome_array(self, head: ListNode) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        j = len(tmp)
        for i in range(0, int(j / 2)):
            if tmp[i] == tmp[j - 1]:
                j = j - 1
                continue
            else:
                return False
        return True
