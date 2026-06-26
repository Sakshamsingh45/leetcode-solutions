class Solution:
    def findWordsContaining(self, words, x):
        a = []
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        
        if len(a) == 0:
            return []
        #elif len(a) == 1:
         #   return [a[0]]
        else:
            return a
