class Solution:
    def binaryGap(self, n: int) -> int:
        dis=0
        flag=False
        while n>0:
            a=n%2
            if flag:
                if a==1:
                    d=1
                else:
                    d+=1
                dis=max(dis,d)
            else:
                if a==1:
                    flag=True
                    d=1
            n=n//2
        return dis