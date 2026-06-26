class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        mcount=0
        for i in range(len(s)):
            a=s[i]
            flag=False
            count=0
            for j in range(i,len(s)):
                if s[j]==a:
                    count+=1
                else:
                    count-=1
                    flag=True

                if flag and s[j]==a:
                    break
                    
                if count==0 :
                    mcount+=1
        return mcount