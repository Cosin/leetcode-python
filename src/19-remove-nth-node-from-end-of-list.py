# @File : 19-remove-nth-node-from-end-of-list.py
# @Author : Shane Shek
# @Date : 2021-01-21 21:56:36
# @Desc : 删除链表的倒数第 N 个结点

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。 
# 
#  进阶：你能尝试使用一趟扫描实现吗？ 
#
#  示例 1： 
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#  示例 2： 
#
# 输入：head = [1], n = 1
# 输出：[]
#
#  示例 3： 
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#  提示：
#
#  链表中结点的数目为 sz 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp = ListNode(-1)
        tmp.next = head
        first = tmp
        second = tmp
        for i in range(0, n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return tmp.next