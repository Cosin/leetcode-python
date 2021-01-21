# @File : 203-remove-linked-list-elements.py
# @Author : Shane Shek
# @Date : 2021-01-21 19:29:11
# @Desc : 移除链表元素

# 删除链表中等于给定值 val 的所有节点。 
# 
#  示例: 
# 
#  输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 设置哨兵节点
        sentinel = ListNode(0)
        sentinel.next = head
        # prev为前置节点，curr为游标，指向判断节点
        prev, curr = sentinel, head
        # 当前节点不为空
        while curr:
            # 当前节点等于目标值，则让prev指向curr的下一个节点
            if curr.val == val:
                prev.next = curr.next
            # 否则，prev移动一个节点
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
