# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Run a DFS and both calculate the height and check balancing.
        # Time complexity: O(n) (dfs on every node)
        # Space complexity: O(h) (call stack as big as tallest branch)
        def dfs(node):
            if not node:
                return [0, True]
            left = dfs(node.left)
            right = dfs(node.right)

            balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            height = 1 + max(left[0], right[0]) 
            
            return [height, balanced]
        
        return dfs(root)[1]