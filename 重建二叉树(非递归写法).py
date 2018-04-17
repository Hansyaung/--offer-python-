'''
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

'''
# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        # 非递归方法思路：每次找一个节点，每个节点对应两个数列pre,tin
        p_head = TreeNode(pre[0])
        ps = [p_head]
        pres = [pre]
        tins = [tin]
        
        while len(ps) > 0:
            ps_new = []
            pres_new = []
            tins_new = []
            #for p in ps:
             #   print(p.val)
            for i,p in enumerate(ps):# 对队列中的每个点，计算其左节点和右节点
                pre = pres[i]
                tin = tins[i]

                # 计算左右子树的中序遍历
                tin_left = []
                tin_right = []
                flag = 0
                for value in tin:
                    if value == p.val:
                        flag = 1
                    elif flag == 0:
                        tin_left += [value]
                    else:
                        tin_right += [value]

                # 计算左右子树的前序遍历
                pre_left = []
                pre_right = []
                flag = 0
                for value in pre:
                    if value in tin_left:
                        pre_left += [value]
                    elif value in tin_right:
                        pre_right += [value]

                # 更新当前节点的左右节点,更新节点队列，更新前序遍历队列，更新中序遍历队列
                if len(pre_left) > 0:
                    p_left = TreeNode(pre_left[0])
                    p.left = p_left
                    ps_new += [p.left]
                    pres_new += [pre_left]
                    tins_new += [tin_left]
                    
                if len(pre_right) > 0:
                    p_right = TreeNode(pre_right[0])
                    p.right = p_right
                    ps_new += [p.right]
                    pres_new += [pre_right]
                    tins_new += [tin_right]

            ps = ps_new
            pres = pres_new
            tins = tins_new
            
        return p_head

if __name__ == '__main__':
    pred = [1,2,4,7,3,5,6,8]
    tins = [4,7,2,1,5,3,8,6]
    ss = Solution()
    p_head = ss.reConstructBinaryTree(pred, tins)

    un_print = [p_head]
    while len(un_print) > 0:
        p = un_print[0]
        print(p.val)
        if p.left is not None:
            un_print += [p.left]
        if p.right is not None:
            un_print += [p.right]
        un_print = un_print[1:]
