'''
题目描述
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) ==0:
            return False
        
        row = 0
        column = len(array[0]) -1
        
        while row <= len(array)-1 and column >= 0:
            if array[row][column] > target:
                column -= 1 # 去掉这一列
                row += 1
            elif array[row][column] == target:
                return True
            else:
        return False
