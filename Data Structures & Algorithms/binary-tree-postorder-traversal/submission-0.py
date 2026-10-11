# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def check(root):
            if root is None:
                return
            check(root.left)
            check(root.right)
            result.append(root.val)
        check(root)
        return result