class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=set()
        ans=set()
        if len(s)<10:
            return []
        l=0
        for r in range(9,len(s)):
            st=s[l:r+1]
            if st in res:
                ans.add(st)
            if st not in res:
                res.add(st)
            l+=1
        return list(ans)