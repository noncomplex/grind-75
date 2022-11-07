# initialize an empty list and a variable -
# the second variable is used to append while the first can
# be returned as a way to keep track of the head and empty list edge cases
# Then simply compare and update references in O(n)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        lst = dummy
        while list1 and list2:
            if list1.val < list2.val:
                lst.next = list1
                list1 = list1.next
            else:
                lst.next = list2
                list2 = list2.next
            lst = lst.next
        
        if list1:
            lst.next = list1
        elif list2:
            lst.next = list2
        
        return dummy.next
