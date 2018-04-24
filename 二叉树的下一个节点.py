# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None 父节点？
class Solution:
    def GetNext(self, pNode):
        # write code here
        # 该节点有右子树，则找到右子树的最左节点
        if pNode.right is not None:
            p = pNode.right # 头结点
            while p.left is not None:
                p = p.left
            return p
        else:
            # pNode 没有右子树
            # 如果pNode在父节点的左侧，则下一节点为父节点
            # 如果pNode在父节点的右侧，则需要沿着树向上，直到找到一个节点为父节点的左节点，然后返回这个父节点
                p = pNode
                while p.next is not None:
                    if p.next.left != p: # 如果不是左节点，则上溯
                        p = p.next
                    else:  # 如果是左节点，则返回其父节点
                        return p.next
                return None
