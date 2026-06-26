class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)   # O(m), where m = len(brokenLetters)
        words = text.split()          # O(n), where n = len(text)
        count = 0
        
        for word in words:            # loop over k words
            if not any(ch in broken for ch in word):
                count += 1
        return count
