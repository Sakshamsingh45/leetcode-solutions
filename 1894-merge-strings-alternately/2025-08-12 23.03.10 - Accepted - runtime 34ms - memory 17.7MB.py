class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=''
        for i in range(min(len(word1),len(word2))):
            final+= word1[i]+word2[i]
        i+=1
        if len(word1)>len(word2):
            while i<len(word1):
                final+=word1[i]
                i+=1
        else:
            while i<len(word2):
                final+=word2[i]
                i+=1
        return final

