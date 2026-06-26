class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        for start in range(len(s)):
            for length in range(len(s),start+1,-1):
                if check(start,length):
                    return s[start :length]

        return ""