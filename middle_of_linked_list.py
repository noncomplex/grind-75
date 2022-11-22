# have a pointer go 1x and another go 2x
# at the end of 2x the 1x pointer is in the middle
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head

        while(b and b.next):
            a = a.next
            b = b.next.next

        return a
