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
