class Solution:
    def sumGame(self, num: str) -> bool:
        countb=sumb=0
        counta=suma=0
        n=len(num)
        for i,j in enumerate(num):
            if i<n//2:
                if j=="?":
                    countb+=1
                else:
                    sumb+=int(j)
            else:
                if j=="?":
                    counta+=1
                else:
                    suma+=int(j)
                
        if countb+counta==0:
            return not(suma==sumb)
        if (counta+countb)%2==1 or (sumb-suma!=(counta-countb)*9//2):
            return True
        else:
            return False
        