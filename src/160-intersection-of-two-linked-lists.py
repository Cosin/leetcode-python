# @File : 160-intersection-of-two-linked-lists.py
# @Author : Shane Shek
# @Date : 2021-12-06 11:10:46
# @Desc : 相交链表

# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。 
# 
#  图示两个链表在节点 c1 开始相交： 
#
#  题目数据 保证 整个链式结构中不存在环。 
#  注意，函数返回结果后，链表必须 保持其原始结构 。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode_0(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        hash表法
        """
        visited = set()
        tmp_node = headA
        while tmp_node:
            visited.add(tmp_node)
            tmp_node = tmp_node.next
        tmp_node = headB
        while tmp_node:
            if tmp_node in visited:
                print(tmp_node.val)
                return tmp_node
            tmp_node = tmp_node.next
        return None

    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        消除长度法
        先遍历找出长度差，再在同起点位置遍历
        """
        len_a = len_b = 0
        tmp_a = headA
        tmp_b = headB
        while tmp_a:
            len_a += 1
            tmp_a = tmp_a.next
        while tmp_b:
            len_b += 1
            tmp_b = tmp_b.next
        tmp_a = headA
        tmp_b = headB
        if len_a > len_b:
            for i in range(0, len_a - len_b):
                tmp_a = tmp_a.next
        else:
            for i in range(0, len_b - len_a):
                tmp_b = tmp_b.next
        while tmp_a:
            if tmp_a is tmp_b:
                return tmp_a
            tmp_a = tmp_a.next
            tmp_b = tmp_b.next
        return None

    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        消除长度法
        通过移动指针，使两指针处于同起点
        """
        tmp_a = headA
        tmp_b = headB
        while tmp_a != tmp_b:
            if tmp_a is None:
                tmp_a = headB
            else:
                tmp_a = tmp_a.next
            if tmp_b is None:
                tmp_b = headA
            else:
                tmp_b = tmp_b.next
        return tmp_a