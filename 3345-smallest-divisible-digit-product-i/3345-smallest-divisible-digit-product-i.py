class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def check(temp):
            m=1
            while temp:
                digit=temp%10
                if digit==0:
                    return True
                m*=digit
                temp//=10
            if m%t==0:
                return True
            return False
        while n:
            flag=check(n)
            if flag:
                return n
            n+=1
