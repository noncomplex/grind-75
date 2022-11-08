# use a dictionary to determine the counts for each char in 1 str
# and use the other str to decrement each occurence
# if every element has a count of 0 then we know it's an anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]] += 1
            elif(s[i] not in d):
                d[s[i]] = 1
            if(t[i] in d):
                d[t[i]] -= 1
            elif(t[i] not in d):
                d[t[i]] = -1
        for c in d:
            if d[c] != 0:
                return False
        return True
