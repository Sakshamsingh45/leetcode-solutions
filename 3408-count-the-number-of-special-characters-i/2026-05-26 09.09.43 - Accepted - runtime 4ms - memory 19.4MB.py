class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        word=set(word)
        for i in word:
            if i.isupper() and i.lower() in word:
                count+=1
            elif i.islower() and i.upper() in word:
                count+=1
        return count//2