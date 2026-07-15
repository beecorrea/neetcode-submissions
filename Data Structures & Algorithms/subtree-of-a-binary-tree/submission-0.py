# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def cmp(p, q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
        
            if bool(p) ^ bool(q):
                return False
            
            if p.val != q.val:
                return False

            return cmp(p.left, q.left) and cmp(p.right, q.right)
        
        if not root:
            return False
        if not subRoot:
            return True

        if cmp(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
