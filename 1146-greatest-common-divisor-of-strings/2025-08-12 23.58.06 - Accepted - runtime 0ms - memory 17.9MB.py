class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # helper function to find gcd of two numbers
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # if concatenation in both orders is different, no gcd string exists
        if str1 + str2 != str2 + str1:
            return ""
        
        length = gcd(len(str1), len(str2))
        return str1[:length]
