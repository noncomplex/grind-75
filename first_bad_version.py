# naively, can use O(n) for loop, but this leads to time limit exceeded
# Can just use binary search with 1 extra check for the return
# if the current version is bad version and the previous isn't

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m) and not(isBadVersion(m-1)):
                return m
            elif isBadVersion(m):
                r = m - 1
            else:
                l = m + 1
