# Many ways to think of this, but most easily imo is similar
# to valid anagram. Character count of each in magazine and
# decrement corresponding characters in ransomNote as they exist

class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for c in magazine:
            if d[c]:
                d[c] += 1
            else:
                d[c] = 1

        for c in ransomNote:
            if d[c] > 0:
                d[c] -= 1
            else:
                return False

        return True
