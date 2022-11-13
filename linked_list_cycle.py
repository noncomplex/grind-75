# Python set operations are O(1) lookup can just iterate
# and check to see if node has been seen before.

# TODO: come back to solve the O(1) memory follow-up question
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevs = set()
        while head:
            if head in prevs:
                return True
            else:
                prevs.add(head)
                head = head.next
        return False
