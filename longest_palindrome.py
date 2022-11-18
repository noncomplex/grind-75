# There's probably a much easier solution, but this is what first came into mind.
# count each character in str and then find the max odd value because the max odd
# value can be used for a odd palindrome where the +1 odd number can be used in
# the middle of the string. Convert every other odd character to even or 0 if +1
# and add to length because all even quantities can be included. Then length + the max
# odd value count can be returned. The tricky part
# is that if there are multiple max_odd values > 1 then (n - 1)*(max_odd - 1) need
# to be included.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        max_odd = 0
        for _, v in d.items():
            if v % 2 != 0 and v > max_odd:
                max_odd = v

        l = 0
        max_odd_count = 0
        for _, v in d.items():
            if v >= 2 and v % 2 == 0:
                l += v
            elif v != max_odd:
                l += v - 1
            elif v == max_odd:
                max_odd_count += 1

        return l + max_odd + abs(max_odd_count - 1) * (max_odd - 1) if max_odd > 0 else l
