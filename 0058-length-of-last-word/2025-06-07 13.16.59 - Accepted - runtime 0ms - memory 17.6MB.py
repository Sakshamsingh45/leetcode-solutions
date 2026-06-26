class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        index = -1
        count = 0

        while -index <= len(s):
            if s[index] == " ":
                break
            count += 1
            index -= 1
        
        return count
