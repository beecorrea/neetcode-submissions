# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Not straightforward to deduce because you have to think of post-order traversal.
        # Main idea is that you have to think of these two patterns in the tree:
        #   - Current node is the LCA
        #   - LCA is in the left or right subtree
        # 1) Run a search for both p and q. 
        # 2) If you can find both nodes from the current node, it means the current node is the LCA.
        # 3) If you can only find one of the nodes, return it to the parent. 
        #    It'll be propagated to the actual LCA.
        # 4) In the end, return the current node (in the worst case, the LCA is the root).
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Edge case
        if not root:
            return None
        
        # If the node itself is the common ancestor, return it.
        if root.val == p.val or root.val == q.val:
            return root

        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)

        if not left_subtree:
            return right_subtree
        if not right_subtree:
            return left_subtree

        return root

