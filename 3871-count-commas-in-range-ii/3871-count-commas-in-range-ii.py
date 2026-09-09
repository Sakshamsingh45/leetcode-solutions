class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        st=1000
        count=0
        cm=1
        while st*1000<=n:
            count+=cm*((st*1000)-st)
            cm+=1
            st*=1000
        count+=cm*(n-st+1)
        return count
