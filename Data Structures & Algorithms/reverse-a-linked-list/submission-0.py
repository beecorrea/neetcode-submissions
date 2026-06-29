# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> null ===> 3 -> 2 -> 1 -> null
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            # Reverse curr's pointer.
            curr.next = prev
            # Advance pointers
            prev = curr
            curr = temp
        
        # Return new head (last node)
        return prev
