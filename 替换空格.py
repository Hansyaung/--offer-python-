'''
题目描述
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        count_space = 0
        s_ret = ''
        for c in s:
            if c == ' ':
                count_space += 1
                s_ret += '%20'
            else:
                s_ret += c
        return s_ret
