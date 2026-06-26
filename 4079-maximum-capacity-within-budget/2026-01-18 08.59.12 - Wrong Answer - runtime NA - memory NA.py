class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        maxcap=None
        for i in range(len(costs)):
            if costs[i]<budget and (maxcap is None or maxcap<capacity[i]):
                maxcap=capacity[i]
            for j in range(i+1,len(costs)):
                if costs[i]+costs[j]<budget and maxcap<capacity[i]+capacity[j]:
                    maxcap=capacity[i]+capacity[j]
        return maxcap
                    
                
                