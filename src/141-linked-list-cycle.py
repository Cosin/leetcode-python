# @File : 141-linked-list-cycle.py
# @Author : Shane Shek
# @Date : 2022-02-10 19:49:30
# @Desc : 环形链表

# 给你一个链表的头节点 head ，判断链表中是否有环。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
# 链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。 
# 
#  如果链表中存在环 ，则返回 true 。 否则，返回 false 。
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 引入额外list，遍历链表节点存入list
    # 判断每个节点是否出现过
    def hasCycle_hash(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

    # 双指针 - 龟兔赛跑
    def hasCycle(self, head: Optional[ListNode],pos) -> bool:
        if head is None or not head.next:
            return False
        head2 = head.next
        while head != head2:
            if not head2 or not head2.next:
                return False
            head = head.next
            head2 = head2.next.next
        return True
