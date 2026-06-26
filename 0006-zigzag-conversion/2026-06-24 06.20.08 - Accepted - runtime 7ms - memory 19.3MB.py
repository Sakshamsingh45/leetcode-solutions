class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        l=[[] for _ in range(numRows)]
        count=0
        dir=1
        for i in s:
            l[count].append(i)
            if count==0:
                dir=1
            elif count==len(l)-1:
                dir=-1
            count+=dir
        ans=""
        for i in l:
            ans+="".join(i)
        return ans