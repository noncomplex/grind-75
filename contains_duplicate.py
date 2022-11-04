# Python set offers O(1) insert and lookup
# therefore checking each element would be O(1) * n = O(n)
# Also O(n) space for the set
# so just iterate and check if each number is in the set
# else add it

def containsDuplicate(self, nums):
    s = set()
    for num in nums:
        if num in s:
            return True
        else:
            s.add(num)
