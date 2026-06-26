class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        dict={}
        factsum=0
        while n>0:
            f=n%10
            dict[f]=dict.get(f,0)+1
            fact=1
            for i in range(1,f+1):
                fact*=i
            factsum+=fact
            n=n//10
        while factsum>0:
            digit=factsum%10
            if dict.get(digit,0)<=0:
                return False
            else:
                dict[digit]=dict.get(digit)-1
            factsum//10
        for i in set(dict.values()):
            if i!=0:
                return False
        return True
            