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
