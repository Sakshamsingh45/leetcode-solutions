class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq=[0]*(max(costs)+1)
        sort=[]
        count=0
        for i in costs:
            freq[i]+=1
        for i in range(len(freq)):
            while freq[i]>0 and coins>=i:
                count+=1
                coins-=i
                freq[i]-=1
        return count