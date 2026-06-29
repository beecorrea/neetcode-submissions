# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        visited = dict()
        curr = head
        while curr:
            if curr.next in visited:
                return True
            # Add to visited
            visited[curr] = i
            i += 1

            # Go to next node
            curr = curr.next

        return False

        