# simply iterate and point the .next value to the previous pointer
# the previous pointer appends the current node to the front,
# thus reversing the array. It's essentially 4 lines of code.
# note nxt is needed to save the next iteration because head.next = prev
# severs that.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        nxt = head
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev
