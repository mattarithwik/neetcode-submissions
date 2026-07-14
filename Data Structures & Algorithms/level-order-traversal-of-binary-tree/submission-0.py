# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            level_size = len(queue)
            this_level = []
            for i in range(level_size):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                this_level.append(popped.val)
            res.append(this_level)
        return res