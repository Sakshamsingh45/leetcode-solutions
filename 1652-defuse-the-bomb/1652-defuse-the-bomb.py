class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[0]*len(code)
        if k==0:
            return ans
        elif k<0:
            code=code[::-1]
        temp=abs(k)
        sm=sum(code[1:1+temp])
        ans=[0]*len(code)
        r=temp
        n=len(code)
        for i in range(n):
            ans[i]=sm
            sm=sm-code[(i+1)%n]+code[(r+1)%n]
            r+=1
        return ans if k>0 else ans[::-1]
        