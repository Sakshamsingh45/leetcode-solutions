class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for i in s:
            if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
                filtered += i.lower() 
        return filtered == filtered[::-1]
