class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        low = chr(0)
        ans = 0
        for s in zip(*strs):
            pre = low
            for c in s:
                if c < pre:
                    ans += 1
                    break
                pre = c
        return ans