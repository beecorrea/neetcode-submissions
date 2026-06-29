# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Recursive
        def do_has_cycle(node, visited):
            if not node:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            return do_has_cycle(node.next, visited)
                
        return do_has_cycle(head, set())

        