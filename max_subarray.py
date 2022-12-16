# basically linearly traverse and keep track of the max sum of sections.
# Sections being elements that have a total positive sum, a new section is started
# when the sums turn negative. Obviously if current subarray sum is negative
# the first future positive element will not need any prior subarrays.

# reminiscent of buy/sell stock; took me awhile to figure out
# until I realized that an empty array (sum of 0) is still a subarray
# obvious that bruteforce quadratic solutions on array problems usually
# can be solved faster, therefore require a bit more thought.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sums = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            max_sum = max(max_sum, cur_sum)
        return max_sum
