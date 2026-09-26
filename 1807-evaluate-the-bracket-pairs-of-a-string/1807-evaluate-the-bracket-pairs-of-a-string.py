class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        freq={}
        for i in knowledge:
            freq[i[0]]=i[1]
        res=""
        i=0
        while i<len(s):
            if s[i]=="(":
                i+=1
                temp=""
                while s[i]!=")":
                    temp+=s[i]
                    i+=1
                if temp in freq:
                    res+=freq[temp]
                else:
                    res+="?"
            else:
                res+=s[i]
            i+=1
        return res
