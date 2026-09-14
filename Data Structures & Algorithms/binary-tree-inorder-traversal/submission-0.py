# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.helper(root, list())

    def helper(self, root, l):
        if not root:
            return l
        if root.left:
            l = self.helper(root.left, l)
        
        l.append(root.val)
        if root.right:
            l = self.helper(root.right, l)
        return l
        