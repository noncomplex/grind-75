# Basic usage of key-value pairs.
# for each number the correct compliment to the target can be easily found.
# knowing that the current index contains the correct summand for a corresponding
# compliment, we can store a key-value pair {compliment : current-index} so
# that if that specific compliment is seen in a future iteration we can return the
# index of that iteration and the stored index.

def twoSum(self, nums, target):
    d = {}
    for i in range(len(nums)):
        num = nums[i]
        comp = target - num
        if num in d:
            return [i, d[num]]
        else:
            d[comp] = i

        
