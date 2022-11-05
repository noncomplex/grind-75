# use for loops to have an array of running products and another for reverse products
# use these to get the left and right products of current index and multiply
# 3 linear loops = O(n)
# right begins at -2 because 1 is appended
#; rprods[right - len(nums) + 1] = -1 index = 1

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        prods = [1]
        rprods = []
        ans = []

        for num in nums:
            prod *= num
            prods.append(prod)
        
        prod = 1
        for num in reversed(nums):
            prod *= num
            rprods.append(prod)
        rprods.append(1)
        
        right = len(prods) - 2
        for i in range(1, len(nums) + 1):
            ans.append(prods[i-1] * rprods[right - i])
        
        return ans
