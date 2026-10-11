# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self,root):
        result=[]
        def check(root):
            if root is None:
                result.append(-1)
                return
            result.append(root.val)
            check(root.left)
            check(root.right)
        check(root)
        return result
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1=self.traverse(p)
        l2=self.traverse(q)
        return l1==l2