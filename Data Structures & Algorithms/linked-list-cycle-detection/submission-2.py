# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            if curr.next in visited:
                return True
            # Add to visited
            visited.add(curr)

            # Go to next node
            curr = curr.next

        return False

        