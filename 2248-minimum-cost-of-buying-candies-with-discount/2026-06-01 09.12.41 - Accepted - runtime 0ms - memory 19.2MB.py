class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        count=0
        left=len(cost)%3
        i=1+left
        while i <len(cost)-1:
            count+=cost[i]+cost[i+1]
            i+=3
        for i in range(left):
            count+=cost[i]
        return count