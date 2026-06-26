class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count=0
        for i in range(len(prices)):
            maxp=prices[i]
            count+=1
            for j in range(i+1,len(prices)):
                if maxp-1!=prices[j]:
                    break
                count+=1
                maxp=prices[j]
        return count

                




        