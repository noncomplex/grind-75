# a solution; pad string with lower length so that
# str a and b are same length. enumerate the possibilities
# with a carry variable. Prepend a 1 if there is a carry
# leftover at the end

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        pad = len(a) - len(b)
        if pad >= 0:
            b = '0' * pad + b
        elif pad < 0:
            a = '0' * abs(pad) + a

        carry = 0
        for i in range(len(a)-1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            if total == 0:
                ans = '0' + ans
                carry = 0
            elif total == 1:
                ans = '1' + ans
                carry = 0
            elif total == 2:
                ans = '0' + ans
                carry = 1
            elif total == 3:
                ans = '1' + ans
                carry = 1

        if carry:
            ans = '1' + ans
        return ans
