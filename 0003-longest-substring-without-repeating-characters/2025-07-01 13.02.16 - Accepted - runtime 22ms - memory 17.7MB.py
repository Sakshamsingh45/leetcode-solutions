class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        max1 = 0

        for char in s:
            if char in stack:
                # Remove all elements before and including the repeated character
                index = stack.index(char)
                stack = stack[index + 1:]

            stack.append(char)
            max1 = max(max1, len(stack))

        return max1
