class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        count=0
        a=[]
        b=[]
        for i in range(len(words)):
            if x in words[i]:
                a.append(i)
        if len(a)==0:
            return []
        elif len(a)==1:
            return [0]
        else:
            return [a[0],a[len(a)-1]]
