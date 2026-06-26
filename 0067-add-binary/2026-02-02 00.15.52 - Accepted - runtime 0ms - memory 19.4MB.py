class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = 0
        ans = ""

        while i < len(a) or i < len(b):
            s = carry

            if i < len(a):
                s += int(a[-1 - i])

            if i < len(b):
                s += int(b[-1 - i])

            if s == 0:
                ans = "0" + ans
                carry = 0
            elif s == 1:
                ans = "1" + ans
                carry = 0
            elif s == 2:
                ans = "0" + ans
                carry = 1
            else:
                ans = "1" + ans
                carry = 1

            i += 1

        if carry:
            ans = "1" + ans

        return ans