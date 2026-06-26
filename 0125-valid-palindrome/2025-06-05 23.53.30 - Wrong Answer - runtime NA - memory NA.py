class Solution:
    def isPalindrome(self, s: str) -> bool:
        self=""
        for i in s:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122:
                self+=i.lower()
        a=self
        b=self[::-1]
        return a==b