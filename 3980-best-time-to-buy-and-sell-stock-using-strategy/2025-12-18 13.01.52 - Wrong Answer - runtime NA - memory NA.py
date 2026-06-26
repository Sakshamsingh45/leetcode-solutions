class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        a=set()
        actualprofit=0
        for i in range(len(prices)):
            actualprofit+=prices[i]*strategy[i]
            if i+k-1<len(prices):
                b=1
                op2profit=0
                while b<=k:
                    if b<k/2:
                        pass
                    else:
                        op2profit+=prices[i+b-1]
                    b+=1
                a.add(op2profit)
        return max(actualprofit,max(a))


        