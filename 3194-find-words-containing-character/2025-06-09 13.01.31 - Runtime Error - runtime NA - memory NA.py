class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count=0
        a=[]
        b=[]
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        if len(a) == 0:
            return []  # or some default value
            else:
                c = min(a)
                b.append(c)
                c = max(a)b.append(c)
