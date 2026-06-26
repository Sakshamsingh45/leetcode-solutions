class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        v = 0  # vowel count
        c = 0  # consonant count

        for ch in word:
            if not ch.isalnum():  # not a letter or digit
                return False

            if ch.isalpha():
                if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
                    v += 1
                else:
                    c += 1

        return v > 0 and c > 0
