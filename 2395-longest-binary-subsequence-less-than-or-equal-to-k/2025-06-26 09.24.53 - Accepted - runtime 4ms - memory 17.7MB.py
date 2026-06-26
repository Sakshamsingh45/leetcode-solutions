class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0       
        power = 1       
        count = 0 
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                if value + power <= k:
                    value += power
                    count += 1
            else: 
                count += 1
            if power <= k:
                power *= 2

        return count
