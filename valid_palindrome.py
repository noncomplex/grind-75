# keep track of left (start from beginning) and right (start from end)
# indices and check each character from them until they reach the middle
# li < ri because middle character doesn't need to be compared
# also need to increment indices for non-alphanumeric values
# O(n/2) = O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        li = 0
        ri = len(s) - 1
        while li < ri:
            if s[li].isalnum() and s[ri].isalnum():
                if s[li].lower() == s[ri].lower():
                    li += 1
                    ri -= 1
                else:
                    return False
            elif not s[li].isalnum():
                li += 1
            elif not s[ri].isalnum():
                ri -= 1
        return True
