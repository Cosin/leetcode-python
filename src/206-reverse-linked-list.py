# @File : 206-reverse-linked-list.py
# @Author : Shane Shek
# @Date : 2021-01-12 14:06:51
# @Desc : 反转链表

# 反转一个单链表。 
# 
#  示例: 
# 
#  输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """双指针"""
        if not head:
            return head
        pre = ListNode(0)
        pre.next = head
        cur = head.next
        while cur:
            head.next = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = head.next
        return pre.next

    def reverseListRecursion(self, head: ListNode) -> ListNode:
        """递归方式"""
        head.print()
        if not head or not head.next:
            return head
        h = self.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        return h
