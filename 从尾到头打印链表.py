'''
题目描述

输入一个链表，从尾到头打印链表每个节点的值。
'''
# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        else:
            ret_list = []
            while listNode.next:
                ret_list += [listNode.val]
                listNode = listNode.next
            ret_list += [listNode.val]
            return ret_list[::-1]
