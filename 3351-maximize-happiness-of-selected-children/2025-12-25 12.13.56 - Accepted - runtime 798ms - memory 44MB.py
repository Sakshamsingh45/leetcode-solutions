class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        count=0
        happiness.sort(reverse=True)
        for i in range(k):
            if happiness[i]-i<0:
                count+=0
                return count
            count+=happiness[i]-i
        return count