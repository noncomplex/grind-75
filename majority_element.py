# naive solution is just iterating and updating the maximum
# count and value.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        maxc, maxn = 0, 0
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
            maxc = max(counts[n], maxc)
            maxn = n if counts[n] == maxc else maxn
        return maxn

    # follow-up O(1) space
    # can just do +1 or -1 on each character because
    # and update on +1 because the majority will always be at
    # a minimum +1 count of any other number
    def majorityElement2(self, nums: List[int]) -> int:
        counts, maxn = 1, 0
        for n in nums:
            if counts == 1:
                maxn = n
            counts += (1 if n == maxn else -1)
        return maxn
