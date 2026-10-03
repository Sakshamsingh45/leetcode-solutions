class Solution:
    def function(self,s):
        l=0
        mcount=0
        count=0
        for r in range(len(s)):
            while count<0:
                if s[l]=="(":
                    count-=1
                else:
                    count+=1
                l+=1
            if s[r]=="(":
                count+=1
            elif s[r]==")":
                count-=1
            if count==0:
                mcount=max(mcount,r-l+1)
        return mcount
    def function2(self,s):
        r=-1
        mcount=0
        count=0
        for l in range(-1,-len(s)-1,-1):
            while count<0:
                if s[r]==")":
                    count-=1
                else:
                    count+=1
                r-=1
            if s[l]==")":
                count+=1
            elif s[l]=="(":
                count-=1
            if count==0:
                mcount=max(mcount,abs(l-r-1))
        return mcount

    def longestValidParentheses(self, s: str) -> int:
        return max(self.function(s),self.function2(s))
            