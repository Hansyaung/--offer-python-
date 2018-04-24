'''
题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
# -*- coding:utf-8 -*-
# 队列为 先进先出
class stack: # 定义栈结构
    def __init__(self):
        self.stack = []
    def isempty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True
        
    def push(self, node):
        # write code here
        self.stack.append(node)

    def pop(self):
        ret = self.stack[-1]
        self.stack = self.stack[:-1]
        return ret # 先进后出

class Solution:
    def __init__(self):
        self.stack_main = stack()
        self.stack_order = stack()

    def push(self, node):
        # write code here
        self.stack_main.push(node)

    def pop(self):
        if self.stack_order.isempty():
            if self.stack_main.isempty():
                return None
            else:
                while not self.stack_main.isempty():
                    self.stack_order.push(self.stack_main.pop())
        return self.stack_order.pop()
