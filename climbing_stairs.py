# at n - 1 and n
# only 1 possible step can be taken
# each subsequent lower n value is just the sum
# of the previous 2 (fibonacci) because those are the
# only options for climbing (+1 or +2)

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            prev = one
            one += two
            two = prev

        return one
