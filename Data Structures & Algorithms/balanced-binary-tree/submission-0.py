# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Calculate the height and check if | h(L) - h(R) | <= 1.
        # Time complexity: O(n^2) (calculate height for every node and check if every node is balanced)
        # Space complexity: O(n) (call stack)
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        if not root:
            return True
        
        l = height(root.left)
        r = height(root.right)

        if abs(l - r) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)