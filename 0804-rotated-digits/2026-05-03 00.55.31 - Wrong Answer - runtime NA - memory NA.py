class Solution:
    def rotatedDigits(self, n: int) -> int:
        no=["2","5","6","9"]
        no=set(no)
        count=0
        for i in range(n+1):
            flag=False
            for j in str(i):
                if j not in no:
                    flag=True
                if flag:
                    break
            if not flag:
                count+=1
        return count