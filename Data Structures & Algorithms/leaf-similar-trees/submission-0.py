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
                return
            if root.left is None and root.right is None:
                result.append(root.val)
            check(root.right)
            check(root.left)
        check(root)
        return result

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=self.traverse(root1)
        l2=self.traverse(root2)
        return l1==l2
        