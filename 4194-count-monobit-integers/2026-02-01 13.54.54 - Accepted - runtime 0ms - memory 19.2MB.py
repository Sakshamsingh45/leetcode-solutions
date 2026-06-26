class Solution:
    def countMonobit(self, n: int) -> int:
        count=1
        i=1
        while i<=n:
            count+=1
            i=i*2+1
        return count