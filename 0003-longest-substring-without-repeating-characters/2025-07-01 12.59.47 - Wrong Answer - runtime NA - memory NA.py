class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack=[]
        max1=0
        for i in s:
            if not stack or i not in stack:
                stack.append(i)
            elif i in stack:
                stack=[]
            max1=max(max1,len(stack))
        return max1
        