class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a=0
        for i in range (0,len(prices)):
            b=prices[i]
            for j in range (i+1,(len(prices))):
                if (prices[j]-b)>a:
                    a=prices[j]-b
        return a